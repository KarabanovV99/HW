from enum import StrEnum
from datetime import date


class ColorEnum(StrEnum):
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    FINISH = "\033[0m"


class Date:
    """representation of the Gregorian calendar and actions with it"""
    arr_days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, day: int = 1, month: int = 1, year: int = 1, before_common_era: bool = False) -> None:
        self.day = day
        self.month = month
        self.year = year
        self.before_common_era = before_common_era

    def input_date(self) -> None:
        """date entry"""
        while True:
            inp_date: str = input(
                "{0}Введите дату в формате День.Месяц.Год(если дата до н.э., то вводите -Год):  {1}".format(
                    ColorEnum.GREEN, ColorEnum.FINISH))
            try:
                self.day, self.month, self.year = map(int, inp_date.split("."))
                if self.year < 0:
                    self.year = abs(self.year)
                    self.before_common_era = True
                else:
                    self.before_common_era = False
                self.validate_date()
                break
            except ValueError:  # input format error
                print("{0}Некорректный формат даты. Пожалуйста, введите дату в формате День.Месяц.Год.{1}".format(
                        ColorEnum.RED, ColorEnum.FINISH))
            except DateValidationError as e:  # custom error
                print(ColorEnum.RED + str(e) + ColorEnum.FINISH)

    @staticmethod
    def is_leap_year(y: int) -> bool:
        """checking leap year"""
        return (y % 4 == 0 and y % 100 != 0) or not y % 400

    @classmethod
    def days_in_month(cls, m: int, y: int):
        """checking the correct number of months"""
        if m == 2 and cls.is_leap_year(y):
            return 29
        m = m % 12
        return cls.arr_days_in_month[m - 1]

    def validate_date(self) -> None:
        """checking the validity of the day and month"""
        if self.year == 0:
            raise DateValidationError("{0}Год 0 не существует (оказывается){1}".format(ColorEnum.RED, ColorEnum.FINISH),
                                      'invalid_year')
        if not 1 <= self.month <= 12:
            raise DateValidationError("{0}Некорректный месяц. Месяц должен быть от 1 до 12."
                                      "{1}".format(ColorEnum.RED, ColorEnum.FINISH), 'invalid_month')
        if not 1 <= self.day <= self.days_in_month(self.month, self.year):
            raise DateValidationError("{0}Некорректный день. Пожалуйста, проверьте количество дней в месяце"
                                      ".{1}".format(ColorEnum.RED, ColorEnum.FINISH), 'invalid_day')

    def add_days(self, days: int) -> None:
        """adding days"""
        days_left = days
        while days_left > 0:
            days_in_month = self.days_in_month(self.month, self.year)
            if self.day + days_left <= days_in_month:
                self.day += days_left
                break
            else:
                days_left -= (days_in_month - self.day + 1)
                self.day = 1
                if self.month == 12:
                    self.month = 1
                    self.year += 1
                else:
                    self.month += 1

    def subtract_days(self, days: int) -> None:
        """subtract days"""
        days_left = days
        while days_left > 0:
            if self.day - days_left >= 1:
                self.day -= days_left
                break
            else:
                days_left -= self.day
                if self.month == 1:
                    self.month = 12
                    self.year -= 1
                else:
                    self.month -= 1
                self.day = self.days_in_month(self.month, self.year)
            if self.year == 0:
                self.year += 1

    def days_from_epoch(self) -> int:
        """calculating the number of days before the start of an epoch"""
        days = 0
        for y in range(1, self.year):
            days += 366 if self.is_leap_year(y) else 365
        for m in range(1, self.month):
            days += self.arr_days_in_month[m - 1]
            if m == 2 and self.is_leap_year(self.year):
                days += 1
        days += self.day - 1
        return days

    def adjust_days(self, days: int) -> None:
        """adjusting days, adding or subtracting based on the sign of days"""
        if days == 0:
            pass
        elif not self.before_common_era and days > 0:
            self.add_days(days)
        elif self.before_common_era and days < 0:
            self.add_days(abs(days))
        else:
            diff = self.days_from_epoch()
            days = abs(days)
            if days < diff:
                self.subtract_days(days)
            else:
                self.day = 1
                self.month = 1
                self.year = 1
                if not self.before_common_era:
                    self.before_common_era = True
                    self.add_days((days - diff) - 1)
                else:
                    self.before_common_era = False
                    self.add_days((days - diff) - 1)

    def day_of_the_week(self) -> str:
        """day of week calculation"""
        sp_year = self.year
        sp_month = self.month
        if self.before_common_era:
            sp_year += 1
        if sp_month < 3:
            sp_month += 12
            sp_year -= 1
        h = (self.day + ((13 * (sp_month + 1)) // 5) + sp_year + (sp_year // 4) - (sp_year // 100) + (
                sp_year // 400)) % 7
        days = ["Суббота", "Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
        return days[h]

    def __str__(self) -> str:
        era_str = "до н.э." if self.before_common_era else ""
        return f'{self.day}.{self.month}.{self.year} {era_str}'

    def __add__(self, other):
        day = self.day + other.day
        month = self.month + other.month
        year = self.year + other.year

        while day > self.days_in_month(month, year):
            day -= self.days_in_month(month, year)
            month += 1

        while month > 12:
            month -= 12
            year += 1

        return __class__(day, month, year)

    def __sub__(self, other):
        day = self.day - other.day
        month = self.month - other.month
        year = self.year - other.year

        if day < 1:
            month -= 1
            if month < 1:
                month += 12
                year -= 1

            days_in_month = self.days_in_month(month, year)
            day += days_in_month

        if month < 1:
            month += 12
            year -= 1

        return __class__(day, month, year)


class DateStamp(Date):
    def __init__(self):
        today = date.today()
        super().__init__(today.day, today.month, today.year)

    def input_date(self):
        raise NotImplementedError


class DateValidationError(Exception):
    """class for beautiful errors"""

    def __init__(self, message, code):
        super().__init__(message)
        self.code = code


if __name__ == "__main__":
    d = DateStamp()
    print(d)
    p = Date(15, 8, 2022)
    t = Date(15, 8, 2)
    print(p)
    print(t)
    print(p - t)
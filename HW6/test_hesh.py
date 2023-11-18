import pytest
from HW6.heshhhhhhhh import *


def test_load():
    size = 10
    table = init_table(size)

    size, table = set_value("key1", "value1", table, size)
    size, table = set_value("key2", "value2", table, size)
    size, table = set_value("key3", "value3", table, size)
    size, table = set_value("key4", "value4", table, size)
    size, table = set_value("key5", "value5", table, size)
    size, table = set_value("key6", "value6", table, size)
    size, table = set_value("key7", "value7", table, size)
    size, table = set_value("key8", "value8", table, size)
    size, table = set_value("key9", "value9", table, size)
    size, table = set_value("key10", "value10", table, size)

    assert load(table) == 0.45


@pytest.mark.parametrize("key, expected",
    [("test", 8),
    ("hello", 2),
    ("world", 2),
    ("python", 4),
    ("java", 8),
    ("c++", 5),
    ("c#", 4),
    ("ruby", 0),
    ("javascript", 9),
    ("php", 8),
    ("", 0),
    (" ", 2),
    ("front_govno", 1),
    ("☠️", 9),
])

def test_hashing(key, expected):
    size = 10

    assert hashing(key, size) == expected


@pytest.mark.parametrize("size, expected",
    [(5, [[], [], [], [], []]),
    (3, [[], [], []]),
    (0, [])])

def test_init_table(size, expected):
    assert init_table(size) == expected


def test_set_value():
    size = 5
    table = init_table(size)

    size, table = set_value("hello", "world", table, size)
    assert table == [[], [], [['hello', 'world']], [], []]
    size, table = set_value("foo", "bar", table, size)
    assert table == [[], [], [['hello', 'world']], [], [['foo', 'bar']]]

def test_get_value():
    size = 5
    table = init_table(size)

    size, table = set_value("hello", "world", table, size)
    value = get_value("hello", table, size)
    assert value == "world"
    size, table = set_value("foo", "bar", table, size)
    value = get_value("foo", table, size)
    assert value == "bar"


def test_del_value():
    size = 5
    table = init_table(size)

    size, table = set_value("hello", "world", table, size)
    table = del_value("hello", table, size)
    assert table == [[], [], [], [], []]
    size, table = set_value("foo", "bar", table, size)
    value = del_value("foo", table, size)
    assert table == [[], [], [], [], []]


def test_resize():
    size = 5
    table = init_table(size)

    size, table = resize(size, table)
    assert size == 10
    assert table == [[], [], [], [], [], [], [], [], [], []]

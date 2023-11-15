import pytest
from HW6.hesh import *


@pytest.mark.parametrize("key,expected",
    [("test", 8),
    ("hello", 2),
    ("world", 2),
    ("python", 4),
    ("java", 8),
    ("c++", 5),
    ("c#", 4),
    ("ruby", 0),
    ("javascript", 9),
    ("php", 8)
])
def test_hash(key, expected):
    assert hash(key) == expected


@pytest.mark.parametrize("key,value",
    [("key1", "value1"),
    ("key2", "value2"),
    ("key3", "value3"),
    ("key4", "value4"),
    ("key5", "value5"),
    ("key6", "value6"),
    ("key7", "value7"),
    ("key8", "value8"),
    ("key9", "value9"),
    ("key10", "value10")
])
def test_set_value(key, value):
    set_value(key, value)
    assert get_value(key) == value


@pytest.mark.parametrize("key,value",
    [("key1", "value1"),
    ("key2", "value2"),
    ("key3", "value3"),
    ("key4", "value4"),
    ("key5", "value5"),
    ("key6", "value6"),
    ("key7", "value7"),
    ("key8", "value8"),
    ("key9", "value9"),
    ("key10", "value10")
])
def test_get_value(key, value):
    set_value(key, value)
    assert get_value(key) == value


@pytest.mark.parametrize("key,value",
    [("key1", "value1"),
    ("key2", "value2"),
    ("key3", "value3"),
    ("key4", "value4"),
    ("key5", "value5"),
    ("key6", "value6"),
    ("key7", "value7"),
    ("key8", "value8"),
    ("key9", "value9"),
    ("key10", "value10")
])
def test_del_value(key, value):
    set_value(key, value)
    del_value(key)
    assert get_value(key) is None


def test_load():
    set_value("key1", "value1")
    set_value("key2", "value2")
    set_value("key3", "value3")
    set_value("key4", "value4")
    set_value("key5", "value5")
    set_value("key6", "value6")
    set_value("key7", "value7")
    set_value("key8", "value8")
    set_value("key9", "value9")
    set_value("key10", "value10")
    assert load() == 0.9

import pytest
from HW6.hesh import Hash


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
    ("php", 8)]
    )
def test_hash(key, expected):
    h = Hash()
    assert h.hash(key) == expected


@pytest.mark.parametrize("key,value", [("key1", "value1"),
    ("key2", "value2"),
    ("key3", "value3"),
    ("key4", "value4"),
    ("key5", "value5"),
    ("key6", "value6"),
    ("key7", "value7"),
    ("key8", "value8"), ("key9", "value9"), ("key10", "value10")
])
def test_set_value(key, value):
    h = Hash()
    h.set_value(key, value)
    assert h.get_value(key) == value


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
    h = Hash()
    h.set_value(key, value)
    assert h.get_value(key) == value


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
("key10", "value10")])
def test_del_value(key, value):
    h = Hash()
    h.set_value(key, value)
    h.del_value(key)
    assert h.get_value(key) is None


def test_load():
    h = Hash()
    h.set_value("key1", "value1")
    h.set_value("key2", "value2")
    h.set_value("key3", "value3")
    h.set_value("key4", "value4")
    h.set_value("key5", "value5")
    h.set_value("key6", "value6")
    h.set_value("key7", "value7")
    h.set_value("key8", "value8")
    h.set_value("key9", "value9")
    h.set_value("key10", "value10")
    assert h.load() == 0.9
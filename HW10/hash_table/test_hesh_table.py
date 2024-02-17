# import pytest
# from hash_table import HashTable


# table_1 = HashTable()
# @pytest.mark.parametrize("key, expected",
#     [("test", 8),
#     ("hello", 2),
#     ("world", 2),
#     ("python", 4),
#     ("java", 8),
#     ("c++", 5),
#     ("c#", 4),
#     ("ruby", 0),
#     ("javascript", 9),
#     ("php", 8)
#     ])
# def test_hash(key, expected):
#     assert table_1.hash(key) == expected

# @pytest.fixture
# def hash_table():
#     return HashTable(10)

# @pytest.mark.parametrize("size", [10, 20, 30])
# def test_init_table(size):
#     hash_table = HashTable(size)
#     assert len(hash_table.table) == size

# def test_set_value(hash_table):
#     hash_table.set_value("key1", "value1")
#     assert hash_table.get_value("key1") == "value1"

# def test_get_value(hash_table):
#     hash_table.set_value("key1", "value1")
#     assert hash_table.get_value("key1") == "value1"
#     assert hash_table.get_value("key2") is None

# def test_del_value(hash_table):
#     hash_table.set_value("key1", "value1")
#     assert hash_table.del_value("key1") is True
#     assert hash_table.del_value("key2") is False

# def test_load(hash_table):
#     hash_table.set_value("key1", "value1")
#     hash_table.set_value("key2", "value2")
#     assert hash_table.load() == 0.2

# def test_str(hash_table):
#     hash_table.set_value("key1", "value1")
#     hash_table.set_value("key2", "value2")
#     assert str(hash_table) == '{"key1": "value1", "key2": "value2"}'

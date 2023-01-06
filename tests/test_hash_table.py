from data_structures.hash_table import HashTable


def test_get_value():
    ht = HashTable(5)
    ht.add_key_value('Jane', 19)
    ht.add_key_value('Ella', 28)
    ht.add_key_value('Luna', 24)
    assert ht.get_value('Luna') == 24
    assert ht.get_value('Jane') == 19
    assert ht.get_value('Ella') == 28
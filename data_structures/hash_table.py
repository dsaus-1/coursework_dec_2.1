class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def custom_hash(self, key):
        """Возвращает целове число (хеш-значение), находящийся в пределах от 0 до table_size"""
        pass

    def add_key_value(self, key, value):
        """
        Добавить новый узел Node(Data(key, value) в хеш-таблицу hash_table[hashed_key]=Node(...)
        При возникновении коллизии строится связанный список.
        """
        pass

    def get_value(self, key):
        """Получить значение (атрибут value класса Data) по ключу key"""
        pass

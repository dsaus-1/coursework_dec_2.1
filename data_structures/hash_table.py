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
        hash_value = (sum(ord(letter) for letter in key) * len(key)) % self.table_size
        return hash_value


    def add_key_value(self, key, value):
        """
        Добавить новый узел Node(Data(key, value) в хеш-таблицу hash_table[hashed_key]=Node(...)
        При возникновении коллизии строится связанный список.
        """
        hashed_key = self.custom_hash(key)
        if not self.hash_table[hashed_key]:
            self.hash_table[hashed_key] = Node(Data(key, value), None)
        else:
            node = self.hash_table[hashed_key]
            while node.next_node:
                node = node.next_node
            node.next_node = Node(Data(key, value), None)


    def get_value(self, key):
        """Получить значение (атрибут value класса Data) по ключу key"""
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key]:
            node = self.hash_table[hashed_key]
            while node.next_node:
                if node.data.key == key:
                    return node.data.value
                node = node.next_node
            return node.data.value


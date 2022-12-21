class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """Дабавляет в бинарное дерево поиска новый узел с данными Node(data)"""
        pass

    def search(self, vacancy_id):
        """
        Возвращает данные о вакансии с полем id, равным vacancy_id.
        Возвращает False, если нет вакансии с id, равным vacancy_id.
        """
        pass

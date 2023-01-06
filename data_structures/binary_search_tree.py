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
        if self.root:
            self._insert_recursive(self.root, data)
        else:
            self.root = Node(data)


    def _insert_recursive(self, node, data):
        if node.data['id'] > data['id']:
            if node.left:
                self._insert_recursive(node.left, data)
            else:
                node.left = Node(data)
        elif node.data['id'] < data['id']:
            if node.right:
                self._insert_recursive(node.right, data)
            else:
                node.right = Node(data)


    def search(self, vacancy_id):
        """
        Возвращает данные о вакансии с полем id, равным vacancy_id.
        Возвращает False, если нет вакансии с id, равным vacancy_id.
        """
        if self.root:
            return self._search_recursive(self.root, vacancy_id)
        return False


    def _search_recursive(self, node, data):
        if node.data['id'] == data:
            return node.data

        if node.data['id'] > data and node.left:
            self._search_recursive(node.left, data)

        if node.data['id'] < data and node.right:
            self._search_recursive(node.right, data)

        return False

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
        if self.root is not None:
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
            return self._search_recursive(vacancy_id, self.root)
        return False


    def _search_recursive(self, vacancy_id, node):
        if vacancy_id == node.data['id']:
            return node.data

        if node.data['id'] > vacancy_id and node.left:
            return self._search_recursive(vacancy_id, node.left)

        elif node.data['id'] < vacancy_id and node.right:
            return self._search_recursive(vacancy_id, node.right)

        return False




if __name__ == '__main__':
    bst = BinarySearchTree()

    bst.insert({'id': 4, 'company_name': 'name'})
    bst.insert({'id': 8, 'company_name': 'name'})
    bst.insert({'id': 2, 'company_name': 'name'})
    bst.insert({'id': 9, 'company_name': 'name'})

    print(bst.search(9))

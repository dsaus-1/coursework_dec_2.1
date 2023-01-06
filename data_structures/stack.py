class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.top = None


    def push(self, data):
        """Добавить элемент в стэк"""
        top_node = Node(data, self.top)
        self.top = top_node


    def pop(self):
        """Удалить элемент из стека и вернуть значение этого элемента"""
        if self.top:
            removed_data = self.top.data
            self.top = self.top.next_node
            return removed_data
        return None


    def to_list(self):
        """Вернуть данные стека в виде списка"""
        list_node = []
        node = self.top
        while node:
            list_node.append(node.data)
            node = node.next_node
        return list_node


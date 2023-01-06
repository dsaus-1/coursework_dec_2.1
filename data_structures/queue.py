class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None


    def enqueue(self, data):
        """Добавить данные в очередь"""
        if self.head is None and self.tail is None:
            self.tail = self.head = Node(data, None)
            return None
        self.tail.next_node = Node(data, None)
        self.tail = self.tail.next_node


    def dequeue(self):
        """Забрать данные из очереди"""
        if self.head is None:
            return None
        removed_data = self.head.data
        self.head = self.head.next_node
        if self.head is None:
            self.tail = None
        return removed_data


    def to_list(self):
        """Вернуть данные очереди в виде списка"""
        list_node = []
        node = self.head
        while node:
            list_node.append(node.data)
            node = node.next_node
        return list_node


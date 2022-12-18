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
        pass

    def dequeue(self):
        """Забрать данные из очереди"""
        pass

    def to_list(self):
        """Вернуть данные очереди в виде списка"""
        pass

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None


    def to_list(self):
        """Возвращает список, содержащий данные узлов связанного списка"""
        list_node = []
        node = self.head
        while node:
            list_node.append(node.data)
            node = node.next_node
        return list_node


    def print_ll(self):
        """Возвращает строку-представление связанного списка для печати"""
        node_list = self.to_list()
        print_str = ''

        for data in node_list:
            if print_str:
                print_str += f'{data} -> '
            else:
                print_str += f'{data} -> '
        print_str += 'None'

        return print_str


    def insert_beginning(self, data):
        """Добавить данные в началов связанного списка"""
        if self.head is None:
            self.head = self.tail = Node(data, None)
            return None

        new_node = Node(data, self.head)
        self.head = new_node


    def insert_at_end(self, data):
        """Добавить данные в конец связанного списка"""
        if self.head is None:
            self.head = self.tail = Node(data, None)
            return None

        self.tail.next_node = Node(data, None)
        self.tail = self.tail.next_node


    def get_vacancy_by_id(self, vacancy_id):
        """Получить данные из связанного списка по id"""
        node = self.head
        while node:
            if node.data['id'] == vacancy_id:
                return node.data
            node = node.next_node
        return None

if __name__ == '__main__':
    ll = LinkedList()
    node3 = Node(1000, None)
    node2 = Node({'id': 1}, node3)
    node1 = Node('data1', node2)
    ll.head = node1

    print(ll.print_ll())
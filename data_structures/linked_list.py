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
        pass

    def print_ll(self):
        """Возвращает строку-представление связанного списка для печати"""
        pass

    def insert_beginning(self, data):
        """Добавить данные в началов связанного списка"""
        pass

    def insert_at_end(self, data):
        """Добавить данные в конец связанного списка"""
        pass

    def get_vacancy_by_id(self, vacancy_id):
        """Получить данные из связанного списка по id"""
        pass

from data_structures.linked_list import LinkedList, Node


def test_print_ll_empty():
    ll = LinkedList()

    assert ll.print_ll() == 'None'


def test_print_ll():
    ll = LinkedList()
    node3 = Node(1000, None)
    node2 = Node({'id': 1}, node3)
    node1 = Node('data1', node2)
    ll.head = node1

    assert ll.print_ll() == "data1 -> {'id': 1} -> 1000 -> None"


def test_insert_beginning():
    ll = LinkedList()
    ll.insert_beginning('data')

    assert ll.print_ll() == 'data -> None'


def test_insert_beginning_twice():
    ll = LinkedList()
    ll.insert_beginning('data2')
    ll.insert_beginning('data1')

    assert ll.print_ll() == 'data1 -> data2 -> None'


def test_insert_at_end():
    ll = LinkedList()
    ll.insert_at_end('data1')

    assert ll.print_ll() == 'data1 -> None'


def test_insert_at_end_twice():
    ll = LinkedList()
    ll.insert_at_end('data1')
    ll.insert_at_end('data2')

    assert ll.print_ll() == 'data1 -> data2 -> None'


def test_insert_at_end_beginning():
    ll = LinkedList()
    ll.insert_at_end('data2')
    ll.insert_beginning('data1')

    assert ll.print_ll() == 'data1 -> data2 -> None'


def test_to_list_empty():
    ll = LinkedList()

    assert ll.to_list() == []


def test_to_list():
    ll = LinkedList()
    ll.insert_beginning('data2')
    ll.insert_beginning('data1')

    assert ll.to_list() == ['data1', 'data2']


def test_get_vacancy_by_id():
    ll = LinkedList()
    ll.insert_beginning({'id': 1, 'key1': 'value1'})
    ll.insert_beginning({'id': 2, 'key2': 'value2'})

    assert ll.get_vacancy_by_id(1) == {'id': 1, 'key1': 'value1'}
    assert ll.get_vacancy_by_id(2) == {'id': 2, 'key2': 'value2'}
    assert ll.get_vacancy_by_id(0) is None

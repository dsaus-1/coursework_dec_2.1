from data_structures.stack import Stack


def test_to_list():
    s = Stack()
    assert s.to_list() == []


def test_push():
    s = Stack()
    s.push('data1')
    s.push({'key': 'value'})
    s.push(1000)

    assert s.to_list() == [1000, {'key': 'value'}, 'data1']


def test_pop_empty():
    s = Stack()
    removed = s.pop()

    assert removed is None


def test_push_pop():
    s = Stack()
    s.push(100)
    removed = s.pop()

    assert removed == 100
    assert s.to_list() == []


def test_push_push_pop():
    s = Stack()
    s.push(100)
    s.push([5])

    assert s.pop() == [5]
    assert s.pop() == 100
    assert s.pop() is None
    assert s.to_list() == []

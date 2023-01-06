from data_structures.queue import Queue


def test_queue_to_list():
    q = Queue()

    assert q.to_list() == []


def test_queue_enqueue():
    q = Queue()
    q.enqueue('data1')
    q.enqueue('data2')

    assert q.to_list() == ['data1', 'data2']


def test_queue_dequeue_empty():
    q = Queue()
    q.dequeue()

    assert q.to_list() == []


def test_queue_dequeue():
    q = Queue()
    q.enqueue('data1')
    q.dequeue()

    assert q.to_list() == []


def test_queue_dequeue2():
    q = Queue()
    q.enqueue('data1')
    q.enqueue('data2')
    q.dequeue()

    assert q.to_list() == ['data2']

from data_structures.binary_search_tree import BinarySearchTree


def test_search_empty():
    bst = BinarySearchTree()
    result = bst.search(1)

    assert result is False


def test_search():
    bst = BinarySearchTree()

    bst.insert({'id': 4, 'company_name': 'name'})
    bst.insert({'id': 8, 'company_name': 'name'})
    bst.insert({'id': 2, 'company_name': 'name'})
    bst.insert({'id': 9, 'company_name': 'name'})

    assert bst.search(9) == {'id': 9, 'company_name': 'name'}
    assert bst.search(4) == {'id': 4, 'company_name': 'name'}
    assert bst.search(1) is False

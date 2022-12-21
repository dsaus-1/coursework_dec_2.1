import random

from linked_list import LinkedList
from hash_table import HashTable
from binary_search_tree import BinarySearchTree
from queue import Queue
from stack import Stack
from connector import Connector


# СВЯЗАННЫЙ СПИСОК
def get_vacancies_descending(vacancy_list):
    """Получить список вакансия в обратном порядке от исходного"""

    all_vacancies_ll = LinkedList()

    for vacancy in vacancy_list:
        all_vacancies_ll.insert_beginning(vacancy)

    return all_vacancies_ll.to_list()


def get_all_vacancies_ascending():
    """Получить список вакансия в исходном порядке от исходного"""

    all_vacancies_ll = LinkedList()

    for vacancy in vacancy_list:
        all_vacancies_ll.insert_at_end(vacancy)

    return all_vacancies_ll.to_list()


def get_one_vacancy(vacancy_list, vacancy_id):
    """Получить вакансию по id"""

    all_vacancies_ll = LinkedList()

    for vacancy in vacancy_list:
        all_vacancies_ll.insert_beginning(vacancy)

    vacancy = all_vacancies_ll.get_vacancy_by_id(vacancy_id)

    return vacancy


# БИНАРНОЕ ДЕРЕВО ПОИСКА
def get_one_vacancy_bst(vacancy_list, vacancy_id):
    random.shuffle(vacancy_list)

    bst = BinarySearchTree()

    for vacancy in vacancy_list:
        bst.insert({
            "id": vacancy.get('id'),  # если в vacancy нет 'id', сгенерировать случайные id (random.shuffle)
            "comany_name": vacancy.get('comany_name'),
            "salary": vacancy.get('salary') * 1.1,
        })

    inflation_adjusted_vacancy = bst.search(vacancy_id)

    if not inflation_adjusted_vacancy:
        return {"message": "vacancy not found"}

    return inflation_adjusted_vacancy


# ОЧЕРЕДЬ
def get_companies_list(vacancy_list):
    q = Queue()

    for vacancy in vacancy_list:
        q.enqueue(vacancy)

    company_list = set()

    for _ in range(len(vacancy_list)):
        vacancy = q.dequeue()
        company = vacancy.get('comany_name')
        company_list.add(company)

    return company_list


# СТЭК
def delete_last_10(vacancy_list):
    s = Stack()

    for vacancy in vacancy_list:
        s.push(vacancy)

    removed_vacancies = []
    for _ in range(10):
        vacancy_to_delete = s.pop()
        removed_vacancies.append(vacancy_to_delete)

    return {"removed": str(removed_vacancies)}


if __name__ == '__main':

    # Получить список вакансий
    vacancy_list = Connector('df.json').select(None)

    # Работа со связанным списком
    all_vacancies_ll = LinkedList()
    for vacancy in vacancy_list:
        all_vacancies_ll.insert_beginning(vacancy)

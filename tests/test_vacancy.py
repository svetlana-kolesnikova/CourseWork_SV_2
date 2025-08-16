import unittest
from src.vacancy import Vacancy

class TestVacancy(unittest.TestCase):
    def test_salary_validation(self):
        salary = {'from': 50000, 'to': 100000, 'currency': 'RUR'}
        v = Vacancy('Программист', 'https://test.ru', salary, 'Описание')
        self.assertEqual(v.salary_from, 50000)
        self.assertEqual(v.salary_to, 100000)

    def test_comparison(self):
        v1 = Vacancy('A', 'link1', {'from': 50000, 'to': 70000, 'currency': 'RUR'}, 'desc')
        v2 = Vacancy('B', 'link2', {'from': 60000, 'to': 80000, 'currency': 'RUR'}, 'desc')
        self.assertTrue(v1 < v2)
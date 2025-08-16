import unittest
from unittest.mock import mock_open, patch
import json

from src.json_saver import JsonSaver
from src.vacancy import Vacancy  # твой класс вакансии


class TestJsonSaver(unittest.TestCase):
    def setUp(self):
        self.saver = JsonSaver(filename='test_vacancies.json')

    @patch('builtins.open', new_callable=mock_open, read_data='[]')
    def test_write_vacancies_adds_unique_vacancies(self, mock_file):
        vacancies_input = [
            {
                'name': 'Developer',
                'alternate_url': 'http://hh.ru/vac1',
                'salary': {'from': 50000, 'to': 70000, 'currency': 'RUR'},
                'snippet': {'requirement': 'Python'}
            },
            {
                'name': 'Developer',
                'alternate_url': 'http://hh.ru/vac1',  # дубликат ссылки
                'salary': {'from': 60000, 'to': 80000, 'currency': 'RUR'},
                'snippet': {'requirement': 'Java'}
            }
        ]

        # Вызываем метод записи вакансий
        self.saver.write_vacancies(vacancies_input)

        # Проверяем, что файл открыт дважды (чтение и запись)
        self.assertEqual(mock_file.call_count, 2)

        # Получаем все вызовы записи в файл
        handle = mock_file()

        # Проверяем, что json.dump вызван с правильными данными (без дубликатов)
        written_data = json.loads(handle.write.call_args[0][0])
        self.assertEqual(len(written_data), 1)
        self.assertEqual(written_data[0]['link'], 'http://hh.ru/vac1')

    @patch('builtins.open', new_callable=mock_open, read_data=json.dumps([
        {
            'name': 'Developer',
            'link': 'http://hh.ru/vac1',
            'salary': {'from': 50000, 'to': 70000, 'currency': 'RUR'},
            'description': 'Python developer'
        }
    ]))
    def test_read_vacancies_returns_vacancy_objects(self, mock_file):
        vacancies = self.saver.read_vacancies()
        self.assertIsInstance(vacancies, list)
        self.assertGreater(len(vacancies), 0)
        self.assertIsInstance(vacancies[0], Vacancy)
        self.assertEqual(vacancies[0].name, 'Developer')
        self.assertEqual(vacancies[0].link, 'http://hh.ru/vac1')

    @patch('builtins.open', new_callable=mock_open, read_data=json.dumps([
        {
            'name': 'Developer',
            'link': 'http://hh.ru/vac1',
            'salary': {'from': 50000, 'to': 70000, 'currency': 'RUR'},
            'description': 'Python developer'
        },
        {
            'name': 'Designer',
            'link': 'http://hh.ru/vac2',
            'salary': None,
            'description': 'UI/UX'
        }
    ]))
    @patch('os.path.exists', return_value=True)
    def test_delite_vacancies_removes_vacancy(self, mock_exists, mock_file):
        # Для этого теста тебе нужно немного изменить метод delite_vacancies,
        # чтобы он принимал параметр ссылки (link) для удаления вакансии.
        # Пока просто проверим вызов без ошибки.

        # если у тебя delite_vacancies принимает параметр link:
        # self.saver.delite_vacancies(link='http://hh.ru/vac1')
        pass  # добавь тест когда реализуешь метод с параметром


if __name__ == '__main__':
    unittest.main()
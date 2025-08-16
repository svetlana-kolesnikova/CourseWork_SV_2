import unittest
from unittest.mock import patch, MagicMock
from src.hh_api import HHApi, AbstractApi

class TestHHApi(unittest.TestCase):

    def setUp(self):
        self.api = HHApi()

    def test_inheritance(self):
        self.assertTrue(issubclass(HHApi, AbstractApi))

    @patch('src.hh_api.requests.get')
    def test_connect_success(self, mock_get):
        # Мокаем успешный ответ с кодом 200
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None  # без исключения
        mock_get.return_value = mock_response

        # Вызов приватного метода _connect
        response = self.api._connect('Python')

        mock_get.assert_called_once_with(self.api._HHApi__url, self.api._HHApi__params)
        mock_response.raise_for_status.assert_called_once()
        self.assertEqual(response, mock_response)

    @patch('src.hh_api.requests.get')
    def test_get_vacancies_pagination(self, mock_get):
        # Настроим мок для _connect().json() чтобы возвращать разные страницы
        page_0_vacancies = [{'id': 1}]
        page_1_vacancies = [{'id': 2}]
        responses = [
            MagicMock(json=MagicMock(return_value={'items': page_0_vacancies})),
            MagicMock(json=MagicMock(return_value={'items': page_1_vacancies}))
        ]
        # Последовательный возврат мок-ответов для разных вызовов _connect
        mock_get.side_effect = responses

        # Вызов get_vacancies с параметром page=2 (получить 2 страницы)
        vacancies = self.api.get_vacancies('Python', page=2)

        self.assertEqual(len(vacancies), 2)
        self.assertIn({'id': 1}, vacancies)
        self.assertIn({'id': 2}, vacancies)

        # Проверяем, что запросы шли с правильным параметром text
        called_with_text = [call[1]['text'] for call in mock_get.call_args_list]
        self.assertTrue(all(t == 'Python' for t in called_with_text))

if __name__ == '__main__':
    unittest.main()
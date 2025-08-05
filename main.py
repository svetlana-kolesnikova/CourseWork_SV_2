from src.hh_api import HHApi
from src.json_saver import JsonSaver
from src.vacancy import Vacancy

hh = HHApi()
raw_vacancies = hh.get_vacancies("Python", page=1)

json_saver = JsonSaver()
json_saver.write_vacancies(raw_vacancies)
# currency = 'RUR'
#
# def filter_by_currency(list_vac, currency):
#     filtered_vac = []
#     for vac in list_vac:
#         if vac['salary']:
#             if vac['salary']['currency'] == currency:
#                 filtered_vac.append(vac)
#     return filtered_vac
#
# filtered_vac = (filter_by_currency(filtered_vacancies, currency))
#
# vacancy_objects = [
#     Vacancy(vac['name'], vac['link'], vac['salary'], vac['description'])
#     for vac in filtered_vac
# ]

# avg_salary = vacancy_objects.__lt__
#
# print(avg_salary)

# if __name__ == '__main__':
    # for vac in vacancy_objects:
    #     print(vac)

    # for vac in filtered_vacancies:
    #     if vac['salary']:
    #         print(vac['salary']['currency'])

#     for vac in vacancy_objects:
#         if vac['salary']['currency'] == 'UZS':
#
#             print(vac)
# #

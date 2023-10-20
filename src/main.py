from interaction_functions import selects_platform, searches_criteria, sort_vacancy, top_vacanсy
from src.saving_vacancies import JSONVacancyStorage

storage = JSONVacancyStorage("vacancies.json")


def user_interaction():
    """Функция для взаимодействия с пользователем"""

    print('Привет! Данная программа производит поиск вакансий на платформах hh.ru и superjob.ru')
    selects_platform()
    searches_criteria()
    print(f'По вашему запросу найдено {storage.len_vacancy()} вакансий')
    sort_vacancies = sort_vacancy()
    top = top_vacanсy()
    if top == False:
        for vac in sort_vacancies:
           print(repr(vac) + '\n')


if __name__ == '__main__':
    user_interaction()
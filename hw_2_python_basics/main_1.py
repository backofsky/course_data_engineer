# Импортируем модули
from requests_tor import RequestsTor
import tqdm
import time
import re
import json
import fake_useragent

from bs4 import BeautifulSoup

# подготовим фейковый заголовок
ua = fake_useragent.UserAgent()

# ссылка для скрапинга hh.ru
url = r'https://hh.ru/search/vacancy?text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&from=suggest_post&salary=&clusters=true&area=113&ored_clusters=true&enable_snippets=true'


def get_html(url):
    """
    Возвращает html-текст со страницы url
    Подаем в класс парсера данные страницы
    """

    # для обхода блокировок
    req = RequestsTor()

    try:
        # запрос страницы
        resp = req.get(url, headers={'User-Agent': ua.random})
    except Exception as e:
        print(e) # Bad Request

    # подали в наш класс парсера данные страницы
    soup = BeautifulSoup(resp.text, "lxml")

    # вывод 
    return soup


def write_data_json(data):
    """
    Запись данных в формате JSON
    """

    # текущая дата, используется для имени файла
    current_time = time.strftime("%d%m%Y")

    # запись
    with open(f"data_{current_time}.json", 'w', encoding='utf-8') as file:
        file.write(json.dumps(data, ensure_ascii=False, indent='\t'))


def get_count_pages(url):
    """
    Количество страниц пагинации
    Входной параметр: объект html-страницы
    """

    html = get_html(url)

    # найдем строку html, где страницы-пагинации
    # ищем класс "pager", потом находим тег "a" и выбираем предпоследний элемент
    count_pages = int(html.find(class_="pager").find_all("a")[-2].text)

    return count_pages


def parser(url):
    """
    Парсер вакансий
    """

    # итоговый список
    data = {
        'data':[]
    }

    # определим количество страниц с вакансией
    count_pages = get_count_pages(url)

    # пробегаем по страницам с помощью цикла
    for page in range(0, count_pages + 1):
        print(f'страница: {page + 1}')

        # раз в 3 секунды будет подаваться запрос
        time.sleep(3)

        # url с нужными страницами
        url_page = f'{url}&page={page}'

        # откроем сответствующую страницу и подадим в класс парсера данные страницы
        soup = get_html(url_page)

        # найдем все вакансии
        tags = soup.find_all(class_="serp-item")

        for item in tqdm.tqdm(tags):

            # cчитаем название вакансии
            tag_name = item.find(attrs={'data-qa':'serp-item__title'})

            # cчитаем регион
            tag_region = item.find(attrs={'data-qa':'vacancy-serp__vacancy-address'})

            # cчитаем url вакансии
            url_object = tag_name.attrs['href']

            # аналогично переменной soup
            soup_object = get_html(url_object)

            # cчитаем требуемый опыт работы
            tag_work = soup_object.find(attrs={"data-qa":"vacancy-experience"})

            # cчитываем зарплату
            try:
                tag_salary = soup_object.find(attrs={"data-qa": "vacancy-salary"})

                # минимальная зарплата
                min_salary = re.findall(r'\d+\s\d+(?=<!-- --> до)', str(tag_salary))[0]

                # максимальная зарплата
                max_salary = re.findall(r'\d+\s\d+(?=<!-- --> <!-- -->)', str(tag_salary))[0]

                if "руб" in tag_salary:
                    tag_salary = f'{min_salary}-{max_salary}РУБ'
                elif "USD" in tag_salary:
                    tag_salary = f'{min_salary}-{max_salary}USD'
                elif "EUR" in tag_salary:
                    tag_salary = f'{min_salary}-{max_salary}EUR'
                else:
                    # не указана валюта
                    tag_salary = f'{min_salary}-{max_salary}'

            except Exception as e:
                print(e)

                # з/п не указана
                tag_salary = None

            # список с данными
            data['data'].append(
                {
                "title": tag_name.text,
                "work experience": tag_work.text,
                "salary": tag_salary,
                "region": tag_region.text
                }
            )

            print(f" обработана {page + 1}/{count_pages}")

            print(' запись данных в формате JSON')
            write_data_json(data)


# основной код
if __name__ == '__main__':
    parser(url)
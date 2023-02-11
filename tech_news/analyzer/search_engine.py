from tech_news.database import find_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    data = find_news()

    return [
        (item['title'], item['url'])
        for item in data
        if title.lower() in item['title'].lower()
    ]


def convert_date(date):
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        return date_obj.strftime('%d/%m/%Y')
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_date(date):
    data = find_news()
    converted_data = convert_date(date)
    return [
            (item['title'], item['url'])
            for item in data
            if converted_data in item['timestamp']
        ]


# Requisito 9
def search_by_category(category):
    data = find_news()

    return [
        (item['title'], item['url'])
        for item in data
        if category.lower() in item['category'].lower()
    ]

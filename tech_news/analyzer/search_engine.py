from tech_news.database import find_news


# Requisito 7
def search_by_title(title):
    data = find_news()

    return [
        (item['title'], item['url'])
        for item in data
        if title.lower() in item['title'].lower()
    ]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""

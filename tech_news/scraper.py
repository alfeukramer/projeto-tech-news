import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    HEADER = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, timeout=3, headers=HEADER)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selec = Selector(html_content)
    complete_selec = selec.css("h2.entry-title ::attr(href)").getall()
    if not complete_selec:
        return []
    else:
        return complete_selec


# Requisito 3
def scrape_next_page_link(html_content):
    selec = Selector(html_content)
    next_page_selec = selec.css(" a.next.page-numbers ::attr(href)").get()
    if not next_page_selec:
        return None
    else:
        return next_page_selec


# Requisito 4
def scrape_news(html_content):
    selec = Selector(html_content)
    url = selec.css("head link[rel='canonical'] ::attr(href)").get()
    title = selec.css("h1.entry-title ::text").get()
    timestamp = selec.css("li.meta-date ::text").get()
    writer = selec.css("span.author > a ::text").get()
    reading_time = selec.css("li.meta-reading-time ::text").get().split()
    category = selec.css("span.label ::text").get()
    summary = selec.css("div.entry-content > p:nth-of-type(1) ::text").getall()

    result = {
        "url": url,
        "title": title.strip(),
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(reading_time[0]),
        "summary": "".join(summary).strip(),
        "category": category,
    }
    return result


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""

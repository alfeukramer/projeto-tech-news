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
        if (len(complete_selec)) == 0:
            return []
        else:
            return complete_selec


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""

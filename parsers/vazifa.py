import requests
from bs4 import BeautifulSoup

def get_vacancies_from_vazifa():
    url = 'https://www.vazifa.tj/vacancies'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = []

    for item in soup.select('.vacancy-item'):
        title_el = item.select_one('.vacancy-title')
        date_el = item.select_one('.vacancy-date')
        link_el = item.select_one('a')

        if not title_el or not date_el or not link_el:
            continue

        if '2025' not in date_el.text:
            continue

        job = {
            "title": title_el.text.strip(),
            "location": "Душанбе",  # временно
            "format": "офис",       # временно
            "requirements": "-",
            "description": "-",
            "contacts": "-",
            "url": f"https://www.vazifa.tj{link_el['href']}"
        }
        jobs.append(job)

    return jobs
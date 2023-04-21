import requests
from bs4 import BeautifulSoup

url = "https://www.fon.bet/sports/?source=4&featured=13"  # Замените на URL сайта, который хотите спарсить

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a")

    for link in links:
        print(link.get("href"))
else:
    print(f"Ошибка при получении данных с сайта. Код ответа: {response.status_code}")

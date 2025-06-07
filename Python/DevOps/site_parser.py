# парсинг HTML-страницы сайта, извлекая заголовок страницы, все ссылки, содержимое таблицы и содержимое определённого блока <div>
import requests  # Импортируем библиотеку для отправки HTTP-запросов
from bs4 import BeautifulSoup  # Импортируем инструмент для парсинга HTML


url = "https://weldering.com/ruchnaya-dugovaya-svarka-mma"  # Указываем URL-адрес сайта, который хотим обработать

response = requests.get(url)  # Отправляем GET-запрос на указанный URL и получаем ответ

# Создаём объект BeautifulSoup для парсинга HTML-страницы
soup = BeautifulSoup(response.text, "html.parser")


title = soup.title.text  # Извлекаем текст из тега <title> (заголовок страницы)
print(f"Title: {title}")  # Выводим заголовок страницы

# print(soup.text)  # Выводим весь текст с веб-страницы, исключая HTML-теги

links = soup.find_all("a")  # Находим все теги <a> (гиперссылки) на странице
for link in links:  # Перебираем найденные ссылки
    # Получаем значение атрибута href (адрес ссылки) и выводим его
    print(link.get("href"))

table = soup.find("table")
rows = table.find_all("tr")
for row in rows:
    columns = row.find_all("td")
    for col in columns:
        print(col.text, end="\t")
    print()

# Ищем div с указанным классом
div_content = soup.find("div", {"class": "region region-sidebar-first"})
# Печатаем содержимое найденного div
print("Content for the div tag:\n", div_content)





from dataclasses import field
from re import search
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
# driver.maximize_window()
# зайти в лабиринт
driver.get('https://www.labirint.ru/')
sleep(5)

# найти книги по слову Python
search_locator = "#search-field"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("Python")
search_input.send_keys(Keys.RETURN)

# собрать все карточки товаров
books = driver.find_elements(By.CSS_SELECTOR, "div.product-card" )

print(len(books))

# вывести в консоль информацию название, автор, цена
# for book in books:
#    try:
#     author = book.find_element(By.CSS_SELECTOR,"div.product-card_author")
#     author = author_element.text
#    except:
#     author = "Автор не указан"
#     print(author)
for book in books:
    title = ""
    author = ""
    price = ""
    try:
        author_element = book.find_element(By.CSS_SELECTOR, "div.product-card__author")
        author = author_element.text
    except Exception as e:
        author = "Автор не указан"
        print(e)  # Вывод ошибки для отладки

    print(author)


# driver.fullscreen_window()
#
sleep(15)
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webelement import WebElement


import sqlite3

DB_NAME = 'biggeek.db'
URL = "https://biggeek.ru/"


def parse_specs(driver: webdriver.Chrome, link: str):
    driver.get(link)
    specs_list: WebElement = driver.find_elements(
        By.CLASS_NAME, 'tabs-content__txt-row')
    specs = {}
    for spec in specs_list:
        try:
            descr: WebElement = spec.find_element(By.CLASS_NAME, 'descr')
            value: WebElement = spec.find_element(By.CLASS_NAME, 'value')
        except Exception:
            continue
        descr = descr.get_attribute('innerHTML')
        if descr.find('<') != -1:
            descr = descr[:descr.find('<')].strip()
        else:
            descr = descr.strip()
        value = value.get_attribute('innerHTML')
        # print(f"{descr}: {value}")
        if descr == 'Страна производства':
            specs['country'] = value
        if descr == 'Операционная система':
            specs['os'] = value
        if descr == 'Цвет':
            specs['color'] = value
        if descr == 'Процессор':
            specs['processor'] = value
        if descr == 'Объем встроенной памяти':
            specs['storage'] = value
        if descr == 'Основная камера':
            specs['camera'] = value.split(',')[0]
    return specs


def parse_card(card: WebElement):
    name = card.find_element(By.CLASS_NAME, 'catalog-card__title').text
    manufacturer = name.split(' ')[1]
    price = card.find_element(By.CLASS_NAME, 'cart-modal-count').text[3:-2]
    price = int(price.replace(" ", ""))
    return name, manufacturer, price


def parse_phones(driver: webdriver.Chrome, link: str):
    driver.get(link)
    cards = driver.find_elements(By.CLASS_NAME, 'catalog-card')
    data = []
    specs = []
    for card in cards:
        phone_info = parse_card(card)
        data.append(phone_info)
        specs_link = card.find_element(By.TAG_NAME, 'a').get_attribute('href')
        specs.append(parse_specs(driver, specs_link))
        break
    return data, specs


def execute_query(db_name: str, query: str):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    result = c.execute(query)
    conn.commit()
    conn.close()
    return result


def select(db_name: str, query: str):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    result = c.execute(query).fetchall()
    conn.commit()
    conn.close()
    return result


def main():
    options = Options()
    options.add_argument("-headless")

    driver = webdriver.Firefox(options=options)

    driver.get(URL)

    phones_count = select(
        DB_NAME, 'SELECT COUNT(*) FROM phones')[0][0]

    sections = driver.find_elements(
        By.CLASS_NAME, 'nav-fixed-header__link')
    for section in sections:
        try:
            href = section.get_attribute('href')
        except Exception:
            continue
        if 'iphone' in href:
            driver.get(href)
            break

    iphone_catalog = driver.find_element(
        By.CLASS_NAME,  'catalog-filter__category')
    iphone_links = iphone_catalog.find_elements(By.TAG_NAME, 'a')
    iphone_links = [link.get_attribute('href') for link in iphone_links]
    iphone_links = filter(lambda x: 'iphone-15' in x, iphone_links)

    for link in iphone_links:
        data, specs = parse_phones(driver, link)
        for row in data:
            query = 'INSERT INTO phones (name, manufacturer, price) VALUES ("{}","{}","{}");'.format(
                *row)
            print(query)
            execute_query(DB_NAME, query)
        for row in specs:
            query = 'INSERT INTO specs (phone_id, country, os, color, storage, processor, camera) VALUES ({},"{}","{}","{}","{}","{}","{}");'.format(
                phones_count + 1, *row.values())
            print(query)
            phones_count += 1
            execute_query(DB_NAME, query)

    driver.quit()


if __name__ == '__main__':
    main()

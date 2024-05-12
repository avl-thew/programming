import pickle
from time import sleep

from icecream import ic
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from undetected_chromedriver import Chrome


def parse_ram(filename: str) -> None:
    driver = Chrome()
    driver.get("https://www.dns-shop.ru/catalog/17a89a3916404e77/operativnaya-pamyat-dimm/")
    counter = 0
    with open(filename, "wb") as file:
        while True:
            sleep(3)
            products = driver.find_elements(
                By.XPATH,
                "//div[@class='catalog-product ui-button-widget ']"
            )

            for i, p in enumerate(products):
                stick = {}
                name = p.find_element(By.XPATH, "a[@class='catalog-product__name ui-link ui-link_black']")
                price = p.find_element(By.XPATH, ".//div[@class='product-buy__price']")
                stick["name"] = name.text.strip()
                stick["price"] = float(''.join(price.text.split()[:-1]))
                counter += 1
                print(counter)
                ic(stick)
                pickle.dump(stick, file)

            try:
                btn_next = driver.find_element(
                    By.XPATH,
                    "//a[@class='pagination-widget__page-link pagination-widget__page-link_next ']"
                )
                btn_next.click()
                
            except NoSuchElementException:
                print("Parsing done!")
                break
    driver.quit()


if __name__ == "__main__":
    parse_ram("sticks.pkl")
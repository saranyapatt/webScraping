from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

if __name__ == "__main__":
    data = []
    driver = webdriver.Chrome()
    driver.get("https://books.toscrape.com/")
    for i in range(50):
        content = wait.until(EC.element_to_be_selected((By.CLASS_NAME, "product_pod")))
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        products = soup.find_all("article", {"class": "product_pod"})

        """add product"""
        for product in products:
            p = product.find("h3")
            content = p.find("a")
            price = product.find("p", {"class": "price_color"})
            temp = {'Book Title': content['title'],
                    'Price': price.text}
            data.append(temp)

        """next page"""
        if i<49:
            next_page = driver.find_element(By.CLASS_NAME, "next")
            link = next_page.find_element(By.TAG_NAME, "a")
            link.click()

    """save data"""
    df = pd.DataFrame(data)
    df.to_excel("book.xlsx", index=False)
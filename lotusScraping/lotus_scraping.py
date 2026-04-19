import pandas as pd
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == '__main__':
    data = []
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.lotuss.com/th")
    wait = WebDriverWait(driver, 3)
    search_input = wait.until(EC.element_to_be_clickable((By.ID, "search-bar-input")))
    search_input.click()
    search_input.send_keys("น้ำดื่มตราสิงห์")
    search_input.send_keys(Keys.ENTER)
    wait = WebDriverWait(driver, 3)
    wait.until(EC.element_to_be_clickable((By.ID, "product-list")))
    for _ in range(10):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    html = driver.page_source
    soup = bs(html, "html.parser")

    item = soup.find_all(class_="MuiTypography-root MuiTypography-body1 mui-style-17swnep")
    price = soup.find_all(class_="mui-style-18s6ztp")
    for i,j in zip(item, price):
        temp = {'สินค้า': i.text,
                'ราคา': j.text}
        data.append(temp)
    df = pd.DataFrame(data)
    df.to_excel("lotus.xlsx", index=False)
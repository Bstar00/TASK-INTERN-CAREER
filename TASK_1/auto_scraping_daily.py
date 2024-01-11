#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import schedule

def wait_for_element(driver, by, value, timeout=10):
    """
    An explicit wait function to wait for an element to be present.
    """
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )

def scrape_data():
    url = 'https://www.thewhiskyexchange.com/'

    # Use a web driver
    driver = webdriver.Chrome()
    driver.get(url)

    try:
        # Wait for the content to load 
        wait_for_element(driver, By.CLASS_NAME, 'product-card__content')

        # Get the updated page source after the content is loaded
        updated_page_source = driver.page_source

        # Use BeautifulSoup on the updated page source
        soup = BeautifulSoup(updated_page_source, 'html.parser')

        # Find the desired elements
        item_list = soup.find_all("div", {"class": "product-card__content"})
        price_list = soup.find_all("div", {"class": "product-card__data"})

        # Iterate over each item to extract product name, price, volume, and purity
        for item, price in zip(item_list, price_list):
            product_name = item.find("p", {"class": "product-card__name"})
            prices = price.find("p", {"class": "product-card__price"})
            meta_info = item.find("p", {"class": "product-card__meta"})

            if product_name and prices and meta_info:
                print("Product Name:", product_name.text.strip())
                print("Price:", prices.text.strip())

                # Extract and print volume and purity
                meta_text = meta_info.text.strip()
                volume_and_purity = meta_text.replace('\n', '').replace(' / ', ' | ')
                print("Volume and Purity:", volume_and_purity)

                print("------")

    finally:
        # Close the WebDriver
        driver.quit()

# Schedule the script to run daily at 12:00
schedule.every().day.at("12:00").do(scrape_data)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)

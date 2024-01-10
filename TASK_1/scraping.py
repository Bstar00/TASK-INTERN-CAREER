#!/usr/bin/python3

import schedule
import time
from selenium import webdriver
from bs4 import BeautifulSoup

def scrape_data():
    url = 'https://www.thewhiskyexchange.com/'

    # Use a web driver
    driver = webdriver.Chrome()
    driver.get(url)

    # Wait for the content to load 
    driver.implicitly_wait(10)

    # Get the updated page source after the content is loaded
    updated_page_source = driver.page_source

    # Close the WebDriver
    driver.quit()

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

# Schedule the script to run daily at a specific time
schedule.every().day.at("12:00").do(scrape_data)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)

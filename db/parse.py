from bs4 import BeautifulSoup
from os.path import basename

import requests
import re


class Parse:
    _type = None
    category_id = {
        'rolly': 1,
        'pizza': 2,
        'deserty': 3,
        'sushi-sety': 4,
        'zakuski': 5
    }

    @staticmethod
    def get_product_links(link: str) -> list:
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'lxml')
        Parse._type = basename(link)
        urls_tag = soup.find('div', {'class': 'products-container'}).findAll('a')
        urls = [link.get('href') for link in urls_tag]
        return urls

    @staticmethod
    def get_product_details(product_link: str) -> list:
        page = requests.get(product_link)
        soup = BeautifulSoup(page.content, 'lxml')
        name = soup.find('span', {'class': 'h2'}).get_text()
        description = soup.find('div', {'class': 'desc'}).get_text()[8:].strip()
        weight = re.findall(r'\d+', soup.find('div', {'class': 'weight'}).get_text())
        price = int(soup.find('span', {'class': 'amount'}).get_text())
        image_link = soup.find('div', {'class': 'product-img'}).find('img').get('src')
        Parse.save_img(image_link)
        image_path = f'db\\image\\{basename(image_link)}'
        category_id = Parse.category_id[Parse._type]
        product_size = 0

        if soup.find('div', {'class': 'variants'}):
            price_30, price_40 = [item['data-price'] for item in soup.findAll('input', {'data-price': True})][:2]
            return [[name, description, int(weight[0]), category_id, price_30, image_path, 30],
                    [name, description, int(weight[1]), category_id, price_40, image_path, 40]]

        return [name, description, int(weight[0]), category_id, price, image_path, product_size]

    @staticmethod
    def save_img(link: str) -> None:
        with open('image\\' + Parse._type + basename(link), 'wb') as f:
            f.write(requests.get(link).content)

    @staticmethod
    def get_products_details(link: str):
        products_details = []
        product_links = Parse.get_product_links(link)

        for url in product_links:
            details = Parse.get_product_details(url)

            if len(details) == 2:
                products_details.append(details[0])
                products_details.append(details[1])
            else:
                products_details.append(details)

        return products_details


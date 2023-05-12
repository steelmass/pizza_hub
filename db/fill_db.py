from db.parse import Parse
from db.crud import DB
from dotenv import load_dotenv
import os

load_dotenv()
db = DB('localhost', 'pizza_hub', 'postgres', os.getenv('DB_PASSWORD'))


class FillDB:
    _categories = ['rolly',
                   'pizza',
                   'deserty',
                   'sushi-sety',
                   'zakuski']
    _link = 'http://roll.lg.ua/catalog/'

    @staticmethod
    def push_products():
        for category in FillDB._categories:
            products = Parse.get_products_details(FillDB._link + category)
            db.insert('product',
                      ['name', 'description', 'weight', 'category_id', 'price', 'image_path', 'product_size'], products)




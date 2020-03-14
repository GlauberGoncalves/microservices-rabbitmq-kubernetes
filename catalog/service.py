from model import Product
import requests

PRODUCTS_URL = os.getenv('PRODUCT_URL')

class ProductService():
    def __init__(self):
        pass

    def find_one(self, uuid):
        try:
            r = requests.get(url=PRODUCTS_URL + "/products/{}".format(uuid))
            return r.json()            
        except:
            print("It's not possible access products microservice")

    def find_all(self):
        try:
            r = requests.get(url=PRODUCTS_URL + "/products")
            return r.json()['products']
        except:
            print("It's not possible access products microservice")
        return []


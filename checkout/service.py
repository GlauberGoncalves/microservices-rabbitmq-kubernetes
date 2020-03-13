from model import Product, Order
from flask import jsonify
import requests

PRODUCTS_URL = "http://localhost:3333/products/"


class ProductService():
    def __init__(self):
        pass

    def find_one(self, uuid):
        try:
            r = requests.get(url=PRODUCTS_URL + uuid)
            return r.json()
        except:
            print("It's not possible access products microservice")


class CheckoutService():

    def generate_order(self, name, email, phone, product_id):
        order = Order(name, email, phone, product_id)
        dic_order = convert_park_to_dict(order)
        return dic_order


def convert_park_to_dict(park):
    park_dict = {}
    for attr in vars(park):
        attr_value = getattr(park, attr)
        if isinstance(attr_value, Order):
            point_dict = vars(attr_value)
            park_dict[attr] = point_dict
        else:
            park_dict[attr] = attr_value
    return park_dict

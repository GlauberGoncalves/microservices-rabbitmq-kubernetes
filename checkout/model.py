class Product():
    def __init__(self, uuid, product, price):
        self.uuid = uuid
        self.product = product
        self.price = price


class Order():
    def __init__(self, name, email, phone, product_id):
        self.name = name
        self.email = email
        self.phone = phone
        self.product_id = product_id

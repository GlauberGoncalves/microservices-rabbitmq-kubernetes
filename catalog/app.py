from flask import Flask, render_template
from service import ProductService

app = Flask(__name__, static_folder="static")

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    return response

@app.route("/products")
def list_products():
    service = ProductService()
    products = service.find_all()    
    return render_template("catalog.html", prodocts = products)


@app.route("/products/<id>")
def show_product(id):
    service = ProductService()
    product = service.find_one(id)
    print(product)
    return render_template("view.html", product = product )

if __name__ == "__main__":
    app.run(port=5000, debug=True) 
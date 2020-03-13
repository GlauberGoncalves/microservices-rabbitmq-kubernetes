from flask import Flask, render_template, request, jsonify, redirect, url_for
from service import ProductService, CheckoutService
from model import Order
import qqueue as queue

app = Flask(__name__, static_folder="static")

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    return response

@app.route("/finish", methods = ['POST'])
def finish():
    data = request.form 
    
    service = CheckoutService()
    order = service.generate_order(data['name'], data['email'], data['phone'], data['product_id'])        

    queue.notify(order)

    return redirect(url_for('success'))


@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/displayCheckout/<id>")
def display_checkout(id):
    service = ProductService() 
    product = service.find_one(id)    
    return render_template("checkout.html", product = product )

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True) 
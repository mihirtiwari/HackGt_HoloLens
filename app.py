from flask import Flask, request
import nutrition
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/process', methods=['GET'])
def process_image():
    return "works"

@app.route('/account/bill=<bill>', methods=['GET'])
def bill(bill):
    return "Bill"

@app.route('/account', methods=['GET'])
def account():
    return "Account"

@app.route('/wishlist', methods=['POST'])
def add_wishlist():
    return "wishlist"

@app.route('/nutrition', methods=['GET'])
def get_nutrition():
    return json.dumps(nutrition.get_nutrition())

if __name__ == "__main__":
    app.run(debug = True)

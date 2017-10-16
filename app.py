from flask import Flask, request
import nutrition, capone, ncr
import json, base64
from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as CImage
from PIL import Image
import io

app = Flask(__name__)
c_app = ClarifaiApp(api_key='be4628bc8c5947eeb93c36ad2f8a27cc')
model = c_app.models.get('gt')

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/process/', methods=['GET', 'POST']) #get item price and return
def process_image():
    # i = '11111111111111111111111111' + '11111100111111111100111111' + '11110001111100111110001111' + '11000001111000011110000011' +'10000000111000011100000001' +'10000000000000000000000001' +'00000000000000000000000000' +'00000000000000000000000000' +'10000000000000000000000001' +'10000110001000010001100001' +'11001111111100111111110011' +'11100111111100111111100111' + '11111111111111111111111111'

    # im = Image.open(io.BytesIO(i))
    # im.show()
    image = request.get_data()

    with open('image.png', 'wb') as f:
        f.write(base64.b64decode(image))

    # image = CImage(url='http://media.npr.org/assets/img/2012/02/04/dietcoke_custom-0473c1516f8a6fd514e84622d0e092ae0172a66c-s300-c85.jpg')
    image = CImage(file_obj=open('./image.png', 'rb'))
    res = model.predict([image])

    # print(res)

    prediction = res['outputs'][0]['data']['concepts'][0]['name']

    item_code = ncr.getItem(prediction)['itemCode']

    price = ncr.getItemPrice(item_code)

    # print(prediction)
    # print(price)

    return json.dumps({"price": price, "item": prediction})

@app.route('/account/bill=<bill>&item=<item>', methods=['GET'])
def bill(bill, item):
    current_bal = capone.getTotalBalance()
    rem_balance = capone.buyProduct(item, bill, current_bal)

    return json.dumps({"balance": rem_balance})

@app.route('/account', methods=['GET'])
def account():
    balance = capone.getTotalBalance()
    return json.dumps({"balance": balance})

@app.route('/wishlist', methods=['POST'])
def add_wishlist():
    return "wishlist"

@app.route('/nutrition', methods=['GET'])
def get_nutrition():
    return json.dumps(nutrition.get_nutrition())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug = True)

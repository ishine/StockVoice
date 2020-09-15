from flask import Flask, jsonify, abort, make_response, request
from flask_cors import CORS
from models.models import Stocks
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route("/apiStockData/<code>")
def stock(code):
    all_stocks = Stocks.query.filter(Stocks.code==code).all()
    result = []
    for stocks in all_stocks:
        result.append(dict(date=stocks.date, open=stocks.open, close=stocks.close, high=stocks.high, low=stocks.low, volume=stocks.volume))
    return make_response(jsonify(result))

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)

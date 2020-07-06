from flask import Flask, jsonify, abort, make_response, request
from flask_cors import CORS
from models.models import Stocks
import json

api = Flask(__name__)
api.config['JSON_AS_ASCII'] = False
CORS(api)

@api.route("/apiStockData/<code>")
def stock(code):
    all_stocks = Stocks.query.filter(Stocks.code==code).all()
    result = []
    for stocks in all_stocks:
        result.append(dict(date=stocks.date, open=stocks.open, high=stocks.high, low=stocks.low, close=stocks.close, volume=stocks.volume))
    #result = '['
    #for stocks in all_stocks:
    #    jsn = '{"date":"' + stocks.date + '",' + '"open":' + str(stocks.open) + ',' + '"high":' + str(stocks.high) + ',' + '"low":' + str(stocks.low) + ',' + '"close":' + str(stocks.close) + ',' + '"volume":' + str(stocks.volume) + '},'
    #    result += jsn
    #result += ']'
    return make_response(jsonify(result))

@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    api.run(host='127.0.0.1', port=8080)

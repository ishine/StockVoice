from flask import Flask, jsonify, abort, make_response, request
from flask_cors import CORS
from models.models import Stocks
import json

api = Flask(__name__)
api.config['JSON_AS_ASCII'] = False
CORS(api)

@api.route("/apiStockData/<code>")
def stock(code):
    result = [  
    {  
        "date":"2018-02-02",
        "open":154.5,
        "high":154.8,
        "low":153.5,
        "close":154.2,
        "volume":4202500.00
    },
    {  
        "date":"2018-02-03",
        "open":157.3,
        "high":159.80,
        "low":156.33,
        "close":158.49,
        "volume":9441600.00
    },
    {  
        "date":"2018-02-04",
        "open":153.3,
        "high":159.80,
        "low":156.33,
        "close":158.49,
        "volume":9441600.00
    },
    {  
        "date":"2018-02-05",
        "open":158.3,
        "high":159.80,
        "low":156.33,
        "close":158.49,
        "volume":9441600.00
    }
    ]
    return make_response(jsonify(result))

@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    api.run(host='127.0.0.1', port=8080)

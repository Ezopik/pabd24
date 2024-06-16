"""House price prediction service"""
from dotenv import dotenv_values
from flask import Flask, request
from flask_cors import CORS
from joblib import load
from flask_httpauth import HTTPTokenAuth
# from src.utils import *
# from utils import *
import time
import numpy as np

"""Demo functions for three type of heavy prediction tasks"""



def predict_io_bounded(area):
    """Emulate io delay"""
    time.sleep(1)
    avg_price = 50_000                 # RUB / m2
    return int(area * avg_price)


def predict_cpu_bounded(area, n=90_000_000):
    """Emulate single thread computation"""
    avg_price = sum([x for x in range(n)]) / n
    return int(area * avg_price)


def predict_cpu_multithread(area, n=5_000_000):
    """Emulate multi thread computation"""
    avg_price = np.mean(np.arange(n))
    return int(area * avg_price)


MODEL_SAVE_PATH = 'models/linear_regression_v01.joblib'

app = Flask(__name__)
CORS(app)

config = dotenv_values(".env")
auth = HTTPTokenAuth(scheme='Bearer')

tokens = {
    config['APP_TOKEN']: "user19",
}

model = load(MODEL_SAVE_PATH)


@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]


def predict(in_data: dict) -> int:
    """ Predict house price from input data parameters.
    :param in_data: house parameters.
    :raise Error: If something goes wrong.
    :return: House price, RUB.
    :rtype: int
    """
    area = float(in_data['area'])
    price = predict_cpu_bounded(area)
    return int(price)


@app.route("/")
def home():
    return '<h1>Housing price service.</h1> Use /predict endpoint'


@app.route("/predict", methods=['POST'])
@auth.login_required
def predict_web_serve():
    """Dummy service"""
    in_data = request.get_json()
    price = predict(in_data)
    area = in_data["area"]
    # price = predict_io_bounded(area)
    return {'price': price}


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
#https://pypi.org/project/websocket_client/
# https://finnhub.io/docs/api/websocket-trades
from time import sleep
from math import isnan
import time
import sys
import datetime
import subprocess
import sys
import os
from subprocess import PIPE, Popen
import traceback
import math
import base64
import json
from time import gmtime, strftime
import random, string
import psutil
import base64
import uuid
import json
import socket 
import time
import logging
import pulsar
from pulsar.schema import *
import websocket
from jsonpath_ng import jsonpath, parse


# Pulsar Message Schema
class Stock (Record):
    symbol = String()
    ts = Float()
    currentts = Float()
    volume = Float()
    price = Float()
    tradeconditions = String()
    uuid = String()


client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer(topic='persistent://public/default/stocks' ,schema=JsonSchema(Stock),properties={"producer-name": "py-stocks","producer-id": "pystocks1" })


def on_message(ws, message):
    # print("MSG:" + message)
    stocks_dict = json.loads(message)

    for stockitem in stocks_dict['data']:
        print(stockitem['p'])
        uuid_key = '{0}_{1}'.format(strftime("%Y%m%d%H%M%S",gmtime()),uuid.uuid4())
        stockRecord = Stock()
        stockRecord.symbol = stockitem['s']
        stockRecord.ts = float(stockitem['t'])
        stockRecord.currentts = float(strftime("%Y%m%d%H%M%S",gmtime()))
        stockRecord.volume = float(stockitem['v'])
        stockRecord.price = float(stockitem['p'])
        stockRecord.tradeconditions = ' '.join(stockitem['c'])
        stockRecord.uuid = uuid_key
        producer.send(stockRecord,partition_key=str(uuid_key))
        print(stockRecord)


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")
    print(close_status_code)
    print(close_msg)


def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"AAPL"}')
    ws.send('{"type":"subscribe","symbol":"AMZN"}')
    ws.send('{"type":"subscribe","symbol":"TSLA"}')
    ws.send('{"type":"subscribe","symbol":"AMD"}')
    ws.send('{"type":"subscribe","symbol":"MSFT"}')
    ws.send('{"type":"subscribe","symbol":"GOOG"}')
    ws.send('{"type":"subscribe","symbol":"META"}')
    ws.send('{"type":"subscribe","symbol":"NVDA"}')
    ws.send('{"type":"subscribe","symbol":"CRM"}')
    ws.send('{"type":"subscribe","symbol":"BABA"}')
    ws.send('{"type":"subscribe","symbol":"PYPL"}')
    ws.send('{"type":"subscribe","symbol":"EA"}')
    # ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
    # ws.send('{"type":"subscribe","symbol":"IC MARKETS:1"}')


if __name__ == "__main__":
    #websocket.enableTrace(True)

    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=TokenFromFinnHub",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

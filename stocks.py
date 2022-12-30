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
    stocks_dict = json.loads(message)

    try:
        if stocks_dict is not None and "data" in stocks_dict:
            for stockitem in stocks_dict['data']:
                try:
                    if stockitem is not None and stockitem['s'] is not None: 
                        print(stockitem['p'])
                        uuid_key = '{0}_{1}'.format(strftime("%Y%m%d%H%M%S",gmtime()),uuid.uuid4())
                        stockRecord = Stock()
                        stockRecord.symbol = stockitem['s']
                        stockRecord.ts = float(stockitem['t'])
                        stockRecord.currentts = float(strftime("%Y%m%d%H%M%S",gmtime()))
                        stockRecord.volume = float(stockitem['v'])
                        stockRecord.price = float(stockitem['p'])
                        stockRecord.tradeconditions = ','.join(stockitem['c'])
                        stockRecord.uuid = uuid_key
                        if ( stockitem['s'] != '' ):
                            producer.send(stockRecord,partition_key=str(uuid_key))
                        print(stockRecord)
                except NameError:
                    print ("skip it")
    except Exception as ex:
        print (ex)

def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed websocket to finnhub ###")
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
    ws.send('{"type":"subscribe","symbol":"WMT"}')
    ws.send('{"type":"subscribe","symbol":"NKE"}')
    ws.send('{"type":"subscribe","symbol":"BRK.B"}')
    ws.send('{"type":"subscribe","symbol":"GOOGL"}')
    ws.send('{"type":"subscribe","symbol":"UNH"}')
    ws.send('{"type":"subscribe","symbol":"JNJ"}')
    ws.send('{"type":"subscribe","symbol":"XOM"}')
    ws.send('{"type":"subscribe","symbol":"JPM"}')
    ws.send('{"type":"subscribe","symbol":"V"}')
    ws.send('{"type":"subscribe","symbol":"HD"}')
    ws.send('{"type":"subscribe","symbol":"LLY"}')
    ws.send('{"type":"subscribe","symbol":"CVX"}')
    ws.send('{"type":"subscribe","symbol":"ABBV"}')
    ws.send('{"type":"subscribe","symbol":"PEP"}')
    ws.send('{"type":"subscribe","symbol":"BAC"}')
    ws.send('{"type":"subscribe","symbol":"KO"}')
    ws.send('{"type":"subscribe","symbol":"MA"}')
    ws.send('{"type":"subscribe","symbol":"AVGO"}')
    ws.send('{"type":"subscribe","symbol":"TMO"}')
    ws.send('{"type":"subscribe","symbol":"COST"}')
    ws.send('{"type":"subscribe","symbol":"CSCO"}')
    ws.send('{"type":"subscribe","symbol":"MCD"}')
    ws.send('{"type":"subscribe","symbol":"ABT"}')
    ws.send('{"type":"subscribe","symbol":"VZ"}')
    ws.send('{"type":"subscribe","symbol":"DIS"}')
    ws.send('{"type":"subscribe","symbol":"BMY"}')
    ws.send('{"type":"subscribe","symbol":"CMCSA"}')
    ws.send('{"type":"subscribe","symbol":"RTX"}')
    ws.send('{"type":"subscribe","symbol":"HON"}')
    ws.send('{"type":"subscribe","symbol":"IBM"}')
    ws.send('{"type":"subscribe","symbol":"CVS"}')
    ws.send('{"type":"subscribe","symbol":"ORCL"}')
    ws.send('{"type":"subscribe","symbol":"CAT"}')
    ws.send('{"type":"subscribe","symbol":"LOW"}')
    ws.send('{"type":"subscribe","symbol":"BLK"}')
    ws.send('{"type":"subscribe","symbol":"MS"}')
    ws.send('{"type":"subscribe","symbol":"BA"}')
    ws.send('{"type":"subscribe","symbol":"INTC"}')
    ws.send('{"type":"subscribe","symbol":"INTU"}')
    ws.send('{"type":"subscribe","symbol":"CB"}')
    ws.send('{"type":"subscribe","symbol":"TMUS"}')
    ws.send('{"type":"subscribe","symbol":"C"}')
    ws.send('{"type":"subscribe","symbol":"DUK"}')
    ws.send('{"type":"subscribe","symbol":"BDX"}')
    ws.send('{"type":"subscribe","symbol":"SLB"}')
    ws.send('{"type":"subscribe","symbol":"MMM"}')
    ws.send('{"type":"subscribe","symbol":"CL"}')
    ws.send('{"type":"subscribe","symbol":"TGT"}')
    ws.send('{"type":"subscribe","symbol":"MRNA"}')
    ws.send('{"type":"subscribe","symbol":"ICE"}')
    ws.send('{"type":"subscribe","symbol":"USB"}')

    print("openned websocket connection to finnhub")
    # ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
    # ws.send('{"type":"subscribe","symbol":"IC MARKETS:1"}')


if __name__ == "__main__":
    #websocket.enableTrace(True)

    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=token",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

# FLiPN-Py-Stocks

finnhub stocks

### Python App

Python application receives websocket stream of JSON arrays and sends individual JSON messages with a JSON schema.

![image](https://raw.githubusercontent.com/tspannhw/FLiPN-Py-Stocks/main/finnhubpystocks.png)

### Raw Data
````

{"data":[{"c":["1","8","24","12"],"p":122.1,"s":"TSLA","t":1672348887195,"v":1},{"c":["1","8","24","12"],"p":122.09,"s":"TSLA","t":1672348887196,"v":4},{"c":["1","8","24","12"],"p":122.09,"s":"TSLA","t":1672348887196,"v":10},{"c":["1","8","24","12"],"p":122.1,"s":"TSLA","t":1672348887196,"v":1},{"c":["1","8","24","12"],"p":122.1,"s":"TSLA","t":1672348887196,"v":2},{"c":["1","8","24","12"],"p":122.1,"s":"TSLA","t":1672348887196,"v":10},{"c":["1","8","24","12"],"p":122.1,"s":"TSLA","t":1672348887198,"v":79},{"c":["1","24","12"],"p":129.58,"s":"AAPL","t":1672348887666,"v":1},{"c":["1","24","12"],"p":129.575,"s":"AAPL","t":1672348887785,"v":1}],"type":"trade"}

{"c":["1","8","24","12"],"p":122.1,"s":"TSLA","t":1672348887195,"v":1}

````


### Data Description

````
data
List of trades or price updates.

s
Symbol.

p
Last price.

t
UNIX milliseconds timestamp.

v
Volume.

c
List of trade conditions. A comprehensive list of trade conditions code can be found here
```

### Consume Pulsar Data

````

bin/pulsar-client consume "persistent://public/default/stocks" -s stocks-reader -n 0


----- got message -----
key:[20221230191756_42a4752d-5f66-4245-8153-a5ec8478f738], properties:[], content:{
 "symbol": "AAPL",
 "ts": 1672427874976.0,
 "currentts": 20221230191756.0,
 "volume": 10.0,
 "price": 128.055,
 "tradeconditions": "1 12",
 "uuid": "20221230191756_42a4752d-5f66-4245-8153-a5ec8478f738"
}
----- got message -----
key:[20221230191756_a560a594-7c12-42e7-a76d-6650a48533e0], properties:[], content:{
 "symbol": "TSLA",
 "ts": 1672427874974.0,
 "currentts": 20221230191756.0,
 "volume": 100.0,
 "price": 120.94,
 "tradeconditions": "",
 "uuid": "20221230191756_a560a594-7c12-42e7-a76d-6650a48533e0"
}

````


### References

* https://finnhub.io/docs/api/authentication
* https://finnhub.io/docs/api/websocket-trades

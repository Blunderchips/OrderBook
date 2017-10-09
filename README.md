OrderBook
=========

Matching engine based on a limit order book written in Python.

Features:
* Standard price-time priority
* Supports both market and limit orders
* Add, cancel, update orders

Requirements:
* bintrees

Usage
=====

Install package:

```
pip install orderbook 
```

Import package:

```python
from orderbook import OrderBook
```

```
from orderbook import OrderBook
```
# Create an order book
```
order_book = OrderBook()
```
# Create some limit orders
```
limit_orders = [{'type' : 'limit', 
                   'side' : 'ask', 
                    'quantity' : 5, 
                    'price' : 101,
                    'trade_id' : 100},
                   {'type' : 'limit', 
                    'side' : 'ask', 
                    'quantity' : 5, 
                    'price' : 103,
                    'trade_id' : 101},
                   {'type' : 'limit', 
                    'side' : 'ask', 
                    'quantity' : 5, 
                    'price' : 101,
                    'trade_id' : 102},
                   {'type' : 'limit', 
                    'side' : 'ask', 
                    'quantity' : 5, 
                    'price' : 101,
                    'trade_id' : 103},
                   {'type' : 'limit', 
                    'side' : 'bid', 
                    'quantity' : 5, 
                    'price' : 99,
                    'trade_id' : 100},
                   {'type' : 'limit', 
                    'side' : 'bid', 
                    'quantity' : 5, 
                    'price' : 98,
                    'trade_id' : 101},
                   {'type' : 'limit', 
                    'side' : 'bid', 
                    'quantity' : 5, 
                    'price' : 99,
                    'trade_id' : 102},
                   {'type' : 'limit', 
                    'side' : 'bid', 
                    'quantity' : 5, 
                    'price' : 97,
                    'trade_id' : 103},
                   ]

```
## Add orders to order book
```
for order in limit_orders:
    trades, order_id = order_book.process_order(order, False)
print(order_book)

```
## Submitting a limit order that crosses the opposing best price will result in a trade
```
crossing_limit_order = {'type': 'limit',
                        'side': 'bid',
                        'quantity': 2,
                        'price': 102,
                        'trade_id': 109}

print(crossing_limit_order)
trades, order_in_book = order_book.process_order(crossing_limit_order, False)
print("Trade occurs as incoming bid limit crosses best ask")
print(trades)
print(order_book)

```
## If a limit crosses but is only partially matched, the remaning volume will be placed in the book as an outstanding order
```
big_crossing_limit_order = {'type': 'limit',
                            'side': 'bid',
                            'quantity': 50,
                            'price': 102,
                            'trade_id': 110}
print(big_crossing_limit_order)
trades, order_in_book = order_book.process_order(big_crossing_limit_order, False)
print("Large incoming bid limit crosses best ask. Remaining volume is placed in book.")
print(trades)
print(order_book)

```
# Market Orders - require that a user specifies a side (bid or ask), a quantity, and their unique trade id
```
market_order = {'type': 'market',
                'side': 'ask',
                'quantity': 40,
                'trade_id': 111}
trades, order_id = order_book.process_order(market_order, False)
print("A market order takes the specified volume from the inside of the book, regardless of price")
print("A market ask for 40 results in:")
print(order_book)
```

Key Functions
=============

Create an Order Book:

```python
order_book = OrderBook()
```

process_order

cancel_order

modify_order

get_volume_at_price

get_best_bid

get_best_ask

Data Structure
==============

Orders are sent to the order book using the process_order function. The Order is created using a quote.

```python
# For a limit order
quote = {
	'type' : 'limit',
    'side' : 'bid', 
    'quantity' : 6, 
    'price' : 108.2, 
    'trade_id' : 001
}
         
# and for a market order:
quote = {
	'type' : 'market',
    'side' : 'ask', 
    'quantity' : 6, 
    'trade_id' : 002
}
```



#!/usr/bin/python

import sys
from orderbook import OrderBook
from six.moves import cStringIO
from builtins import input
from decimal import Decimal
import importlib

if __name__ == '__main__':
    def process_line(order_book, line):
        tokens = line.strip().split(",")
        d = {"type" : "limit",
             "side" : "bid" if tokens[0] == 'B' else 'ask',
             "quantity": int(tokens[1]),
             "price" : Decimal(tokens[2]),
             "trade_id" : tokens[3]}
        return order_book.process_order(d, False, False)
                
    
    order_book = OrderBook()
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print("usage: %s input.csv [algo]" % sys.argv[0])
        sys.exit(0)
    if len(sys.argv) == 3:
        myalgomodule = importlib.import_module(sys.argv[2])
        myalgo = myalgomodule.Algorithm(order_book)
    else:
        myalgo = None
    try:
        reader = open(sys.argv[1], 'r')
        for line in reader:
            trades = None
            order = None
            if line[0] == '#':
                next
            elif line[0] == 'B' or line[0] == 'A':
                (trade, order) = process_line(order_book, line)
                myalgo.trade_stats(trade, 'trade')
            # Manual Debugging
            print ("\n")
            print ("Input: " + line)
            print (order_book)
            print (myalgo.stats())

            if myalgo != None:
                (algo_orders, mode) = myalgo.process_order(line,
                                                           trade, order)
                for line in algo_orders:
                    if line['type'] == 'cancel':
                        order_book.cancel_order(line['side'],
                                                line['order_id'])
                    else:
                        (trade, order) = order_book.process_order(line,
                                                                  False,
                                                                  False)
                        myalgo.trade_stats(trade, mode)
                if len(algo_orders) > 0:
                    print("\n")
                    print("After algo")
                    print(order_book)
                    print (myalgo.stats())

            input("Press enter to continue.")
        reader.close()
    except IOError:
        print ('Cannot open input file "%s"' % sys.argv[1])
        sys.exit(1)

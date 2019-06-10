#!/usr/bin/python

import argparse
import math
import copy
infinity = math.inf


class Ledger:
    __init__(self, buy=infinity, sell=-infinity, best=None):
        self.buy = buy,
        self.sell = sell,
        self.money = sell_at(sell),
        self.best = None

    def sell_at(value):
        self.sell = value
        self.money = sell-buy


def find_max_profit(prices):

    def recursively_profit(prices, money=Ledger()):
        mo = money

        for i, v in enumerate(prices):
            if mo['money'] == -infinity:
                if v < mo['buy']:
                    mo['buy'] = v
                elif v > mo['sell']:
                    mo.sell_at(v)
            elif mo['money'] != -infinity:
                if v > mo['sell']:
                    mo.sell_at(v)
                elif v < mo['buy']:
                    recursively_profit(prices[k:])

    recursively_profit(prices)

    return


if __name__ == '__main__':
    print(find_max_profit([10, 7, 5, 8, 11, 9]))

    # This is just some code to accept inputs from the command line
    # parser = argparse.ArgumentParser(
    #     description='Find max profit from prices.')
    # parser.add_argument('integers', metavar='N', type=int,
    #                     nargs='+', help='an integer price')
    # args = parser.parse_args()

    # print("${profit} profit can be made from sequence: {prices}.".format(
    #     profit=find_max_profit(args.integers), prices=args.integers))

#!/usr/bin/python

import argparse
array = [1, 2, 3, 4, 5, 10]


def find_max_profit(prices):
  profit = prices[1] - prices[0]  # Price of day2 - day1 = profit
  # Loop through all prices using enumerate for indexes
  for index, i in enumerate(prices):
    for p in prices[index + 1:]:  # Slicing the array
      newprofit = p - i
      if newprofit > profit:
        profit = newprofit
  return profit




if __name__ == '__main__':
  # You can test your implementation by running
  # `python stock_prices.py [prices]` where prices is comprised of
  # space-separated integer values
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

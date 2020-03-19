#!/usr/bin/python

import argparse

def find_max_profit(prices):
  cur_min = prices[0]
  min_index = 0
  cur_max = 0
  max_index = 0
  maxlist = prices[1:] # Max can't be first index
  
  for i in range(len(maxlist)):
    if maxlist[i] > cur_max: 
      cur_max = maxlist[i]
      max_index = i
  
  for i in range(len(prices[:max_index+1])):
    if prices[i] < cur_min:
      cur_min = prices[i]
      min_index = i
  
  return cur_max - cur_min


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
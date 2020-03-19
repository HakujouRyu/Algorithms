#!/usr/bin/python

import sys
def helper(n, move=0, ls=[]):
  if move > 2 or n < 1: return []
  moves = ['rock', 'paper', 'scissors']
  print(f'ls: {ls}, move: {moves[move]}')
  ls += [moves[move]] 
  ls = ls + helper(n, move+1, ls)
  return ls
  

    
  


def rock_paper_scissors(n):
  if n == 0: return [[]]
  return helper(n)


if __name__ == "__main__":
  # if len(sys.argv) > 1:
  #   num_plays = int(sys.argv[1])
  #   print(rock_paper_scissors(num_plays))
  # else:
  #   print('Usage: rps.py [num_plays]')
  print(rock_paper_scissors(1))
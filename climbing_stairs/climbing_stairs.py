#!/usr/bin/python

import sys


def climbing_stairs(n, cache=None):
  if not cache:
    # If cache has no value, default cache to an array of zeroes
    cache = [0 for i in range(n+1)]

  if n < 2:
      return 1
  elif n == 2:
      return 2
  elif cache[n] > 2:  # If more than 2 steps, return the value of cache
      return cache[n]  # cache[n] is number of ways we can get to n
  cache[n] = climbing_stairs(n-1, cache) + climbing_stairs(n-2, cache) + \
      climbing_stairs(n-3, cache)
  return cache[n]



if __name__ == "__main__":
  # Test out your implementation from the command line
  # with `python climbing_stairs.py [n]` with different n values
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')

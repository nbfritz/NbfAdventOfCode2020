from functools import partial
from lib.loaders import load_file_as_ints


def find_pair_for_sum(target_sum, rows):
  targets = set()
  for value in rows:
    diff = target_sum - value
    if diff in targets:
      return ({value, diff}, value * diff)
    else:
      targets.add(value)
  return (None, None)    


def find_trio_for_sum(target_sum, rows):
  for value in rows:
    diff = 2020 - value
    pair, total = find_pair_for_sum(diff, rows[1:])
    if pair:
      return ({value,} | pair, value * total) 


def load_data():
  return load_file_as_ints("day1.txt")


part1 = partial(find_pair_for_sum, 2020)
part2 = partial(find_trio_for_sum, 2020)


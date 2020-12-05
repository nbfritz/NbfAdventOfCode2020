import re
from lib.loaders import load_file_as_strings

def _parse_row(row):
    val1_val2, character, passwd = row.replace(":", "").split(" ")
    val1, val2 = [int(v) for v in val1_val2.split("-")]
    return val1, val2, character, passwd

def count_by_incidents(rows):
  def _test(row):
    val1, val2, character, passwd = _parse_row(row)
    count = passwd.count(character)
    return count >= val1 and count <= val2

  return sum(1 if _test(row) else 0 for row in rows)
  

def count_by_position(rows):
  def _test(row):
    val1, val2, character, passwd = _parse_row(row)
    return (passwd[val1 - 1] == character) ^ (passwd[val2 - 1] == character)

  return sum(1 if _test(row) else 0 for row in rows)
  

def load_data():
  return load_file_as_strings("day2.txt")


def part1(data):
  return count_by_incidents(data)


def part2(data):
  return count_by_position(data)
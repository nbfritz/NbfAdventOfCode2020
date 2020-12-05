from lib.loaders import load_file_as_strings

def _parse_pass_id(id):
  binary = id.translate(str.maketrans("FBLR", "0101"))
  return int(binary[:-3], 2), int(binary[-3:], 2), int(binary, 2)


def find_highest_pass_id(data):
  return max(_parse_pass_id(p)[2] for p in data)


def find_missing_pass_id(data):
  seats = {_parse_pass_id(p)[2] for p in data}
  valid = set(range(min(seats), max(seats)))
  return list(valid - seats)[0]


def load_data():
  return load_file_as_strings("day5.txt")


part1 = find_highest_pass_id
part2 = find_missing_pass_id

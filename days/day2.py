from lib.loaders import load_file_as_strings


def _parse_row(row):
    val1_val2, character, passwd = row.replace(":", "").split(" ")
    val1, val2 = [int(v) for v in val1_val2.split("-")]
    return val1, val2, character, passwd


def _validate_by_incidents(row):
    val1, val2, character, passwd = _parse_row(row)
    count = passwd.count(character)
    return count >= val1 and count <= val2


def _validate_by_position(row):
  val1, val2, character, passwd = _parse_row(row)
  return (passwd[val1 - 1] == character) ^ (passwd[val2 - 1] == character)


def count_by_incidents(rows):
  return sum(1 if _validate_by_incidents(row) else 0 for row in rows)
  

def count_by_position(rows):
  return sum(1 if _validate_by_position(row) else 0 for row in rows)
  

def load_data():
  return load_file_as_strings("day2.txt")


part1 = count_by_incidents
part2 = count_by_position
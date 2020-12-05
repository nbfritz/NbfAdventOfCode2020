from lib.loaders import as_strings
import days.day2 as day


DATA = as_strings("""
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
""")


def test_parse_row():
  assert day._parse_row("1-3 a: abcde") == (1, 3, "a", "abcde")
  assert day._parse_row("1-3 b: cdefg") == (1, 3, "b", "cdefg")
  assert day._parse_row("2-9 c: ccccccccc") == (2, 9, "c", "ccccccccc")


def test_validate_by_incidents():
  assert day._validate_by_incidents("1-3 a: abcde") == True
  assert day._validate_by_incidents("1-3 b: cdefg") == False
  assert day._validate_by_incidents("2-9 c: ccccccccc") == True


def test_count_by_incidents():
  assert day.count_by_incidents(DATA) == 2


def test_validate_by_position():
  assert day._validate_by_position("1-3 a: abcde") == True
  assert day._validate_by_position("1-3 b: cdefg") == False
  assert day._validate_by_position("2-9 c: ccccccccc") == False


def test_count_by_position():
  assert day.count_by_position(DATA) == 1


def test_load_data():
  data = day.load_data()
  assert data[0] == "3-11 z: zzzzzdzzzzlzz"


def test_final_results():
  data = day.load_data()
  assert day.part1(data) == 550
  assert day.part2(data) == 634

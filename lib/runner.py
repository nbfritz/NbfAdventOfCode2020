import re
import importlib
import pytest


def parse_input(day_input):
  return re.sub(
    "(\d+)-(\d+)", 
    lambda p: ",".join(str(i) for i in range(int(p.group(1)), int(p.group(2)) + 1)), 
    day_input.replace(" ", "")
  ).split(",")


def run_single_day(day_number):
  try: 
    day = importlib.import_module(f"days.day{day_number}")
  except ModuleNotFoundError:
    print("That day isn't implemented yet.")
    exit()
    
  data = day.load_data()
  print(f"Part 1: {day.part1(data)}")
  print(f"Part 2: {day.part2(data)}")
    

def test_single_day(day_number):
  pytest.main([f"tests/test_day{day_number}.py"])


def run_days(day_numbers):
  for day_number in day_numbers:
    print("\n")
    print("*"*80)
    print(f"RUNNING DAY {day_number}")
    print("*"*80)

    test_single_day(day_number)
    run_single_day(day_number)
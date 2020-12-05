from lib.runner import parse_input, run_days

day_input = input("What day or days should I run (ie. 1,4-5,8)? ")
run_days(parse_input(day_input))
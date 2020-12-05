import string
from lib.loaders import load_file_as_blocks

RULES = dict(
  byr=lambda v: len(v) == 4 and 1920 <= int(v) <= 2002,
  iyr=lambda v: len(v) == 4 and 2010 <= int(v) <= 2020,
  eyr=lambda v: len(v) == 4 and 2021 <= int(v) <= 2030,
  hgt=lambda v: (
    (v[-2:] == "cm" and 150 <= int(v[:-2]) <= 193) or 
    (v[-2:] == "in" and 59 <= int(v[:-2]) <= 76)
  ),
  hcl=lambda v: len(v) == 7 and v[0] == "#" and all(c in string.hexdigits for c in v[1:]),
  ecl=lambda v: v in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
  pid=lambda v: len(v) == 9 and all(c in string.digits for c in v),
  cid=lambda _: True
)
REQD_FIELDS = set(RULES) - {"cid",}


def _parse_block(block):
  return dict(((p[:3], p[4:]) for p in block.split(" ") if p))


def _has_required_fields(record):
  return set(record) & REQD_FIELDS == REQD_FIELDS


def _passes_rules(record):
  return all(k in RULES and RULES[k](v) for k, v in record.items())


def load_data():
  return load_file_as_blocks("day4.txt")


def part1(data):
  parsed = [_parse_block(b) for b in data]
  return sum(1 if _has_required_fields(d) else 0 for d in parsed)


def part2(data):
  parsed = [_parse_block(b) for b in data] 
  return sum(1 if _has_required_fields(d) and _passes_rules(d) else 0 for d in parsed)
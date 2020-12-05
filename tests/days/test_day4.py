from lib.loaders import as_blocks
import days.day4 as day

DATA = as_blocks("""
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
""")


def test_parse_block():
  results = day._parse_block(
    "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
  )
  assert results == dict(
    ecl="gry",
    pid="860033327",
    eyr="2020",
    hcl="#fffffd",
    byr="1937",
    iyr="2017",
    cid="147",
    hgt="183cm",
  )


def test_has_required_fields():
  valid_records = map(day._parse_block, [ 
    "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm",
    "hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm",
  ])
  assert all(day._has_required_fields(r) for r in valid_records)

  invalid_records = map(day._parse_block, [ 
    "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929",
    "hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in",
  ])
  assert not any(day._has_required_fields(r) for r in invalid_records)


def test_passes_rules():
  valid_records = map(day._parse_block, [ 
    "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f",
    "eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
    "hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022",
    "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"
  ])
  assert all(day._passes_rules(r) for r in valid_records)

  invalid_records = map(day._parse_block, [
    "eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
    "iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946",
    "hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
    "hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007",
  ]) 
  assert not any(day._passes_rules(r) for r in invalid_records)
  

def test_count_records_with_required_fields():
  assert day.count_records_with_required_fields(DATA) == 2


def test_count_fully_valid_records():
  assert day.count_fully_valid_records(DATA) == 1


def test_load_data():
  data = day.load_data()
  assert data[0] == (
    "iyr:2015 hgt:59cm byr:2029 cid:219 pid:9381688753 "
    "eyr:1992 hcl:#b6652a ecl:#7a0fa6"
  )


def test_final_results():
  data = day.load_data()
  assert day.part1(data) == 210
  assert day.part2(data) == 121
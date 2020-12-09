import days.day8 as day

DATA = [
  ("nop", 0),
  ("acc", 1),
  ("jmp", 4),
  ("acc", 3),
  ("jmp", -3),
  ("acc", -99),
  ("acc", 1),
  ("jmp", -4),
  ("acc", 6),
]


def test_nop():
  machine = day._build_machine([("nop", 0)])
  new_machine = day._step(machine)
  assert new_machine["instruction"] == 1
  assert new_machine["accumulator"] == 0


def test_acc():
  machine = day._build_machine([("acc", 10)])
  new_machine = day._step(machine)
  assert new_machine["instruction"] == 1
  assert new_machine["accumulator"] == 10


def test_jmp():
  machine = day._build_machine([("jmp", 3)])
  new_machine = day._step(machine)
  assert new_machine["instruction"] == 3
  assert new_machine["accumulator"] == 0


def test_simulate():
  assert day.simulate(DATA) == (1, 5)


def test_mutate_and_simulate():
  assert day.mutate_and_simulate(DATA) == (9, 8)


def test_load_data():
  data = day.load_data()
  assert data[0] == ("acc", -15)


def test_final_results():
  data = day.load_data()
  assert day.part1(data) == (443, 1200)
  assert day.part2(data) == (643, 1023)
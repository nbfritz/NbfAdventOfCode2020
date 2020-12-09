from copy import copy

from lib.loaders import load_file_as_strings


OP_MAPPING = dict(
  acc=lambda m, p: dict(m, accumulator=m["accumulator"] + p),
  nop=lambda m, _: m,
  jmp=lambda m, p: dict(m, instruction=m["instruction"] + p - 1)
)


def _build_machine(program):
  return dict(
    program=program,
    instruction=0,
    accumulator=0,
  )


def _step(machine):
  op, param = machine["program"][machine["instruction"]]
  op_code = OP_MAPPING[op]
  new_machine = op_code(machine, param)
  return dict(new_machine, instruction=new_machine["instruction"] + 1)


def _parse_lines(lines):
  def _parse_line(line):
    pair = line.split(" ")
    return (pair[0], int(pair[1]))
  return [_parse_line(line) for line in lines]


def simulate(data):
  stack = set()
  machine = _build_machine(data)
  while (
    machine["instruction"] not in stack and 
    machine["instruction"] < len(machine["program"])
  ):
    stack.add(machine["instruction"])
    machine = _step(machine)
  return machine["instruction"], machine["accumulator"]


def mutate_and_simulate(data):
  for i, (op, param) in enumerate(data):
    if op not in ["nop", "jmp"]:
      continue

    new_data = copy(data)
    new_data[i] = ("nop", param) if op == "jmp" else ("jmp", param)
    instruction, accumulator = simulate(new_data)

    if instruction == len(data):
      return (instruction, accumulator)


def load_data():
  return _parse_lines(load_file_as_strings("day8.txt"))


part1 = simulate
part2 = mutate_and_simulate
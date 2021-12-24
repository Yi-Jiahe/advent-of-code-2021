import pytest

import day_24.main as day24


@pytest.mark.parametrize("x_val, y_val", [
    (1, 1),
    (2, 5),
    (6, 9)
])
def test_add(x_val, y_val):
    alu = day24.ALU()
    alu.instructions = day24.parse_input(str.splitlines(f"""add x {x_val}
    add y {y_val}
    add z x
    add z y"""))
    alu.input = ""
    alu.run()
    assert alu.vars['x'] == x_val
    assert alu.vars['y'] == y_val
    assert alu.vars['z'] == x_val + y_val


@pytest.mark.parametrize("input", [(str(i)) for i in range(1, 9 + 1)])
def test_alu_negate_x(input):
    alu = day24.ALU()
    alu.instructions = day24.parse_input(str.splitlines("""inp x
mul x -1"""))
    alu.input = input
    alu.run()
    assert alu.vars['x'] == -int(input)


@pytest.mark.parametrize("input, expected_z", [
    ("13", 1),
    ("14", 0),
    ("95", 0)
])
def test_alu_three_times(input, expected_z):
    alu = day24.ALU()
    alu.instructions = day24.parse_input(str.splitlines("""inp z
inp x
mul z 3
eql z x"""))

    alu.input = input
    alu.run()
    assert alu.vars['z'] == expected_z


@pytest.mark.parametrize("input, expected_bits", [(str(i), bin(i)[2:].zfill(4)) for i in range(1, 10)])
def test_alu_binarize(input, expected_bits):
    alu = day24.ALU()
    alu.instructions = day24.parse_input(str.splitlines("""inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2"""))
    alu.input = input
    alu.run()
    assert alu.vars['z'] == int(expected_bits[-1])
    assert alu.vars['y'] == int(expected_bits[-2])
    assert alu.vars['x'] == int(expected_bits[-3])
    assert alu.vars['w'] == int(expected_bits[-4])


def test_input():
    model_number = "13579246899999"

    alu = day24.ALU()
    alu.instructions = day24.parse_input(open("../day_24/puzzle_input.txt", 'r'))
    alu.input = model_number
    alu.run()
    assert alu.input == ""
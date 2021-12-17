import day_17.main as day17


x_range, y_range = day17.parse_input(str.splitlines("""target area: x=20..30, y=-10..-5"""))


def test_part_1():
    assert day17.find_best_height(x_range, y_range) == 45

def test_part_2():
    assert day17.find_suitable_velocities(x_range, y_range) == 112
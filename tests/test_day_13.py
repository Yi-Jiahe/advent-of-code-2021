import day_13.main as day13


def test_part_1():
    dots, folds = day13.parse_input(str.splitlines("""6,10
    0,14
    9,10
    0,3
    10,4
    4,11
    6,0
    6,12
    4,1
    0,13
    10,12
    3,4
    3,0
    8,4
    1,10
    2,14
    8,10
    9,0

    fold along y=7
    fold along x=5"""))
    dots = day13.fold_instructions(dots, folds)


def test_part_2():
    dots, folds = day13.parse_input(str.splitlines("""6,10
    0,14
    9,10
    0,3
    10,4
    4,11
    6,0
    6,12
    4,1
    0,13
    10,12
    3,4
    3,0
    8,4
    1,10
    2,14
    8,10
    9,0

    fold along y=7
    fold along x=5"""))
    dots = day13.fold_instructions(dots, folds)
    day13.print_dots(dots)
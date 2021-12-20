import day_20.main as day20

image_enhancement_algorithm, light_pixels = day20.parse_input(str.splitlines("""..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""))


def test_parse_input():
    assert light_pixels == {(0, 0),
                            (3, 0),
                            (0, 1),
                            (0, 2),
                            (1, 2),
                            (4, 2),
                            (2, 3),
                            (2, 4),
                            (3, 4),
                            (4, 4)}


def test_find_image_bounaries():
    x_min, x_max, y_min, y_max = day20.find_image_boundaries(light_pixels)
    assert x_min == 0
    assert x_max == 4
    assert y_min == 0
    assert y_max == 4


def test_part_one():
    l = {pixel for pixel in light_pixels}
    for i in range(2):
        l = day20.enhance_image(image_enhancement_algorithm, l, i+1)

    assert len(l) == 35


def test_part_two():
    l = {pixel for pixel in light_pixels}
    for i in range(50):
        l = day20.enhance_image(image_enhancement_algorithm, l, i+1)

    assert len(l) == 3351
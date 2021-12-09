import day_9.main as day9

example = """2199943210
3987894921
9856789892
8767896789
9899965678"""

heightmap = day9.parse_input(str.splitlines(example))


def test_parser():
    assert heightmap == [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
                         [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
                         [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
                         [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
                         [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]]


def test_sum_risk_levels():
    total_risk_level = day9.sum_risk_levels(heightmap)
    assert total_risk_level == 15


def test_count_basins():
    basins = day9.find_basin_sizes([[height for height in row] for row in heightmap])

    assert basins == [14, 9, 9, 3]
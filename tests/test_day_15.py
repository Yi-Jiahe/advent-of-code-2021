import day_15.main as day15


risk_levels = day15.parse_input(str.splitlines("""1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""))


def test_part_1():
    start = (0, 0)
    end = (len(risk_levels) - 1, len(risk_levels[0]) - 1)
    total_risk_level_of_lowest_risk_path = day15.search(start, end, risk_levels)

    assert total_risk_level_of_lowest_risk_path == 40


def test_part_2():
    start = (0, 0)
    end = ((len(risk_levels) * 5) - 1, (len(risk_levels[0]) * 5) - 1)
    total_risk_level_of_lowest_risk_path = day15.search_part_2(start, end, risk_levels)

    assert total_risk_level_of_lowest_risk_path == 315

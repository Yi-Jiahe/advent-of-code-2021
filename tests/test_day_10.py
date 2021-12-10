import day_10.main as day10


example = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""
navigation_subsystem = day10.parse_input(str.splitlines(example))


def test_scoring():
    checker_score, stack = day10.parse_line("{([(<{}[<>[]}>{[]{[(<()>")
    assert checker_score == 1197
    checker_score, stack = day10.parse_line("[[<[([]))<([[{}[[()]]]")
    assert checker_score == 3
    checker_score, stack = day10.parse_line("[{[{({}]{}}([{[{{{}}([]")
    assert checker_score == 57
    checker_score, stack = day10.parse_line("[<(<(<(<{}))><([]([]()")
    assert checker_score == 3
    checker_score, stack = day10.parse_line("<{([([[(<>()){}]>(<<{{")
    assert checker_score == 25137


def test_part_one():
    score = 0
    for line in navigation_subsystem:
        line_score, stack = day10.parse_line(line)
        score += line_score
    assert score == 26397


def test_part_two():
    scores = []
    for line in navigation_subsystem:
        _, stack = day10.parse_line(line)
        if stack is not None:
            scores.append(day10.complete_line(stack))
    score = day10.get_middle_score(scores)
    assert score == 288957

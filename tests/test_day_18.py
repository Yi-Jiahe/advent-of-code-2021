import pytest

import day_18.main as day18


@pytest.mark.parametrize("number, exploded, expected_result", [
    ([[[[[9,8],1],2],3],4], True, [[[[0,9],2],3],4]),
    ([7,[6,[5,[4,[3,2]]]]], True, [7,[6,[5,[7,0]]]]),
    ([[6,[5,[4,[3,2]]]],1], True, [[6,[5,[7,0]]],3]),
    ([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]], True, [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]),
    ([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]], True, [[3,[2,[8,0]]],[9,[5,[7,0]]]]),
    ([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]], True, [[[[0,7],4],[7,[[8,4],9]]],[1,1]]),
    ([[[[0,7],4],[7,[[8,4],9]]],[1,1]], True, [[[[0,7],4],[15,[0,13]]],[1,1]]),
    ([[[[0,7],4],[[7,8],[0,13]]],[1,1]], False, [[[[0,7],4],[[7,8],[0,13]]],[1,1]]),
    ([[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]], True, [[[[0,7],4],[[7,8],[6,0]]],[8,1]])
])
def test_explode(number, exploded, expected_result):
    assert day18.explode(number) == exploded
    assert number == expected_result


@pytest.mark.parametrize("number, split_performed, expected_result", [
    ([[[[0,7],4],[15,[0,13]]],[1,1]], True, [[[[0,7],4],[[7,8],[0,13]]],[1,1]]),
    ([[[[0,7],4],[[7,8],[0,13]]],[1,1]], True, [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]),
])
def test_split(number, split_performed, expected_result):
    assert day18.split(number) == split_performed
    assert number == expected_result


@pytest.mark.parametrize("number, expected_result", [
    ([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]], [[[[0,7],4],[[7,8],[6,0]]],[8,1]]),
])
def test_reduce(number, expected_result):
    day18.reduce(number)
    assert number == expected_result


@pytest.mark.parametrize("number, expected_result", [
    ([[1,2],[[3,4],5]], 143),
    ([[[[0,7],4],[[7,8],[6,0]]],[8,1]], 1384),
    ([[[[1,1],[2,2]],[3,3]],[4,4]], 445),
    ([[[[3,0],[5,3]],[4,4]],[5,5]], 791),
    ([[[[5,0],[7,4]],[5,5]],[6,6]], 1137),
    ([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]], 3488),
    ([[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]], 4140)
])
def test_magnitude(number, expected_result):
    assert day18.magnitude(number) == expected_result


@pytest.mark.parametrize("homework, expected_result", [
    ("""[1,1]
[2,2]
[3,3]
[4,4]""", [[[[1,1],[2,2]],[3,3]],[4,4]]),
    ("""[1,1]
[2,2]
[3,3]
[4,4]
[5,5]""", [[[[3,0],[5,3]],[4,4]],[5,5]]),
    ("""[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]""", [[[[5,0],[7,4]],[5,5]],[6,6]]),
    ("""[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]""", [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]),
    ("""[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]""", [[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]])
])
def test_add_numbers(homework, expected_result):
    answer = day18.add_numbers(day18.parse_input(str.splitlines(homework)))
    assert answer == expected_result



def test_part_one():
    answer = day18.part_one(day18.parse_input(str.splitlines("""[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]""")))
    assert answer == 4140



def test_part_two():
    answer = day18.part_two(day18.parse_input(str.splitlines("""[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
    [[[5,[2,8]],4],[5,[[9,9],0]]]
    [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
    [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
    [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
    [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
    [[[[5,4],[7,7]],8],[[8,3],8]]
    [[9,3],[[9,9],[6,[4,9]]]]
    [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
    [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]""")))
    assert answer == 3993
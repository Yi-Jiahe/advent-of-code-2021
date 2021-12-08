import pytest

import day_8.main as day8

example = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

observations = day8.parse_input(str.splitlines(example))


def test_split_patterns_by_length_known_answers():
    signal_patterns = [v.copy() for v in day8.digit_segments.values()]
    digits, five_segments, six_segments = day8.split_patterns_by_length(signal_patterns)
    assert digits[1] == day8.digit_segments[1]
    assert digits[4] == day8.digit_segments[4]
    assert digits[7] == day8.digit_segments[7]
    assert digits[8] == day8.digit_segments[8]

    assert day8.digit_segments[2] in five_segments
    assert day8.digit_segments[3] in five_segments
    assert day8.digit_segments[5] in five_segments

    assert day8.digit_segments[0] in six_segments
    assert day8.digit_segments[6] in six_segments
    assert day8.digit_segments[9] in six_segments


def test_split_patterns_by_length():
    for observation in observations:
        digits, five_segments, six_segments = day8.split_patterns_by_length(observation["unique signal patterns"])
        assert len(digits[1]) == 2
        assert len(digits[4]) == 4
        assert len(digits[7]) == 3
        assert len(digits[8]) == 7
        assert len(five_segments) == 3
        assert len(six_segments) == 3


def test_add_segment():
    segments = day8.digit_segments[7]
    new_segments = day8.add_segment(segments, 'g')
    assert new_segments == {'a', 'c', 'f', 'g'}
    assert new_segments != segments


def test_add_segment_already_in_segments():
    segments = day8.digit_segments[7]
    try:
        new_segments = day8.add_segment(segments, 'a')
        assert False
    except Exception:
        assert True


def test_remove_segment():
    segments = day8.digit_segments[8]
    new_segments = day8.remove_segment(segments, 'e')
    assert new_segments != segments
    assert new_segments == day8.digit_segments[9]


def test_add_segment_not_in_segments():
    segments = day8.digit_segments[1]
    try:
        new_segments = day8.remove_segment(segments, 'd')
        assert False
    except Exception:
        assert True


def test_get_9_from_six_segments():
    arrangements = [
        [0, 6, 9],
        [0, 9, 6],
        [6, 0, 9],
        [6, 9, 0],
        [9, 0, 6],
        [9, 6, 0]
    ]
    arrangements = [[day8.digit_segments[i].copy() for i in arrangement] for arrangement in arrangements]
    for six_segments in arrangements:
        digits = {
            4: day8.digit_segments[4].copy()
        }
        mappings = {
            'a': 'a'
        }
        digits, mappings, six_segments = day8.get_9_from_six_segments(digits, mappings, six_segments)
        assert digits[9] == day8.digit_segments[9]
        assert mappings['g'] == 'g'
        assert day8.digit_segments[0] in six_segments
        assert day8.digit_segments[6] in six_segments
        assert day8.digit_segments[9] not in six_segments


def test_get_e_from_8_and_9():
    digits = {
        8: day8.digit_segments[8].copy(),
        9: day8.digit_segments[9].copy()
    }
    mappings = {}
    mappings = day8.get_e_from_8_and_9(digits, mappings)
    assert mappings['e'] == 'e'


def test_get_2_from_five_segments():
    arrangements = [
        [2, 3, 5],
        [2, 5, 3],
        [3, 2, 5],
        [3, 5, 2],
        [5, 2, 3],
        [5, 3, 2]
    ]
    arrangements = [[day8.digit_segments[i].copy() for i in arrangement] for arrangement in arrangements]
    for five_segments in arrangements:
        digits = {}
        mappings = {
            'e': 'e'
        }
        digits, mappings, six_segments = day8.get_2_from_five_segments(digits, mappings, five_segments)
        assert digits[2] == day8.digit_segments[2]
        assert day8.digit_segments[2] not in five_segments
        assert day8.digit_segments[3] in five_segments
        assert day8.digit_segments[5] in five_segments


def test_get_5_and_3_from_five_segments():
    arrangements = [
        [3, 5],
        [5, 3]
    ]
    arrangements = [[day8.digit_segments[i].copy() for i in arrangement] for arrangement in arrangements]
    for five_segments in arrangements:
        digits = {
            7: day8.digit_segments[7].copy()
        }
        mappings = {
            'g': 'g'
        }
        digits, mappings, five_segments = day8.get_5_and_3_from_five_segments(digits, mappings, five_segments)
        assert digits[3] == day8.digit_segments[3]
        assert digits[5] == day8.digit_segments[5]
        assert mappings['d'] == 'd'
        assert len(five_segments) == 0


def test_get_0_from_8_minus_d():
    arrangements = [
        [0, 6],
        [6, 0]
    ]
    arrangements = [[day8.digit_segments[i].copy() for i in arrangement] for arrangement in arrangements]
    for six_segments in arrangements:
        digits = {
            8: day8.digit_segments[8].copy()
        }
        mappings = {
            'd': 'd'
        }
        digits, six_segments = day8.get_0_from_8_minus_d(digits, mappings, six_segments)
        assert digits[0] == day8.digit_segments[0]
        assert six_segments.pop(0) == day8.digit_segments[6]


# @pytest.mark.skip(reason="testing function not working")
def test_correct_translation():
    answers = [
        "8394",
        "9781",
        "1197",
        "9361",
        "4873",
        "8418",
        "4548",
        "1625",
        "8717",
        "4315"
    ]

    for observation, answer in zip(observations, answers):
        mapping = day8.match_wires_to_segments(observation["unique signal patterns"])
        output = ""
        for digit in observation["four digit output value"]:
            for k, v in mapping.items():
                if digit == v:
                    output += str(k)
        assert output == answer

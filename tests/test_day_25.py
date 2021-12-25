import day_25.main as day25


def test_part_one():
    assert day25.part_one(*day25.parse_input(str.splitlines(
        """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""))) == 58

import pytest

import day_12.main as day12


@pytest.mark.parametrize("cave, expected", [
    ('start', True),
    ('end', True),
    ('A', False),
    ('b', True),
    ('YK', False),
    ('io', True)
])
def test_is_small_cave(cave, expected):
    assert day12.is_small_cave(cave) == expected


@pytest.mark.parametrize("input, n, expected_paths", [
    ("""start-A
start-b
A-c
A-b
b-d
A-end
b-end""", 10, """start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,end
start,A,c,A,b,A,end
start,A,c,A,b,end
start,A,c,A,end
start,A,end
start,b,A,c,A,end
start,b,A,end
start,b,end"""),
    ("""dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""", 19, """start,HN,dc,HN,end
start,HN,dc,HN,kj,HN,end
start,HN,dc,end
start,HN,dc,kj,HN,end
start,HN,end
start,HN,kj,HN,dc,HN,end
start,HN,kj,HN,dc,end
start,HN,kj,HN,end
start,HN,kj,dc,HN,end
start,HN,kj,dc,end
start,dc,HN,end
start,dc,HN,kj,HN,end
start,dc,end
start,dc,kj,HN,end
start,kj,HN,dc,HN,end
start,kj,HN,dc,end
start,kj,HN,end
start,kj,dc,HN,end
start,kj,dc,end"""),
    ("""fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW""", 226, """"""),
])
def test_example_1(input, n, expected_paths):
    edges = day12.parse_input(str.splitlines(input))
    paths = day12.add_path([], "start", edges)
    paths = set([tuple(path) for path in paths])
    assert len(paths) == n
    for path in str.splitlines(expected_paths):
        path = tuple([cave for cave in path.split(',')])
        assert path in paths
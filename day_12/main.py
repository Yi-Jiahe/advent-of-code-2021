from aoc_logging import logger


title = "--- Day 12: Passage Pathing ---"


def parse_input(iterable):
    edges = dict()
    for line in map(lambda line: line.strip(), iterable):
        node_a, node_b = [node for node in map(lambda x: x.strip(), line.split('-'))]
        if node_a not in edges:
            edges[node_a] = set()
        edges[node_a].add(node_b)
        if node_b not in edges:
            edges[node_b] = set()
        edges[node_b].add(node_a)

    return edges


def is_small_cave(cave):
    if str.islower(cave):
        return True
    elif str.isupper(cave):
        return False
    else:
        raise ValueError


def add_path(path, cave, edges):
    if cave in path:
        if is_small_cave(cave):
            return []

    path.append(cave)

    if cave == "end":
        return [path]

    paths = []
    for attached_cave in edges[cave]:
        paths.extend(add_path(path.copy(), attached_cave, edges))
    return paths


def explore_part_2(path, cave, edges, doubled):
    if cave in path:
        if cave == "start":
            return []
        if is_small_cave(cave):
            if not doubled:
                doubled = True
            else:
                return []

    path.append(cave)

    if cave == "end":
        return [path]

    paths = []
    for attached_cave in edges[cave]:
        paths.extend(explore_part_2(path.copy(), attached_cave, edges, doubled))
    return paths



def part_one():
    logger.info(title)
    logger.info("--- Part One ---")
    print("--- Part One ---")

    paths = add_path([], "start", edges)

    print(len(paths))

    logger.info("")


def part_two():
    logger.info(title)
    logger.info("--- Part Two ---")
    print("--- Part Two ---")

    paths = explore_part_2([], "start", edges, False)
    print(len(paths))

    logger.info("")


if __name__ == '__main__':
    print(title)

    edges = None
    with(open("map.txt", 'r')) as f:
        edges = parse_input(f)

    part_one()
    part_two()

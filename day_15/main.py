import math

from aoc_logging import logger


title = "--- Day 15: Chiton ---"

Position = tuple[int, int]


def parse_input(iterable):
    risk_levels = []
    for line in map(lambda line: line.strip(), iterable):
        row = []
        for char in line:
            row.append(int(char))
        risk_levels.append(row)
    return risk_levels


class Node:
    def __init__(self, position: Position, parent, g: int, h: int):
        self.position = position
        self.parent = parent
        self.g = g
        self.h = h
        self.f = self.g + self.h


class PriorityQueue:
    def __init__(self, initial_queue=None):
        if initial_queue is None:
            initial_queue = []
        self.queue = initial_queue

    def __contains__(self, position: Position):
        for element in self.queue:
            if element.position == position:
                return True
        return False

    def get_index_of_lowest_element(self):
        min_i = 0

        min_f = math.inf
        for i, element in enumerate(self.queue):
            if element.f < min_f:
                min_f = element.f
                min_i = i
        return min_i

    def pop_lowest_priority(self):
        return self.queue.pop(self.get_index_of_lowest_element())

    def get_lowest_priority(self):
        return self.queue[self.get_index_of_lowest_element()]

    def get_by_position(self, position: Position):
        for element in self.queue:
            if element.position == position:
                return element

    def remove_by_position(self, position: Position):
        for i, element in enumerate(self.queue):
            if element.position == position:
                break
        return self.queue.pop(i)

    def append(self, node):
        self.queue.append(node)

    def __bool__(self):
        return bool(self.queue)


def compute_movement_cost(position, risk_levels):
    x, y = position
    return risk_levels[y][x]


def compute_h(position, end):
    x, y = position
    end_x, end_y = end
    return abs(end_x - x) + abs(end_y - y)


def search(start, end, risk_levels):
    rows, cols = len(risk_levels), len(risk_levels[0])

    # A* search
    open = PriorityQueue([Node(start, None, 0, compute_h(start, end))])
    closed = set()

    while open.get_lowest_priority().position != end and open:
        current = open.pop_lowest_priority()
        closed.add(current.position)
        for direction in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            x, y = current.position
            x_adj = x + direction[0]
            y_adj = y + direction[1]
            if x_adj < 0 or cols <= x_adj or y_adj < 0 or rows <= y_adj:
                continue
            neighbour = (x_adj, y_adj)
            cost = current.g + compute_movement_cost(neighbour, risk_levels)
            if neighbour in open:
                if cost < open.get_by_position(neighbour).g:
                    open.remove_by_position(neighbour)
            if neighbour not in open and neighbour not in closed:
                neighbour_node = Node(neighbour, current, cost, compute_h(neighbour, end))
                open.append(neighbour_node)

    node = open.get_lowest_priority()
    return node.g


def compute_movement_cost_part_2(position, risk_levels):
    rows, cols = len(risk_levels), len(risk_levels[0])

    x, y = position

    additional_risk_level = x // cols + y // rows

    x %= cols
    y %= rows

    movement_cost = risk_levels[y][x] + additional_risk_level
    if movement_cost > 9:
        movement_cost -= 9
    return movement_cost


def search_part_2(start, end, risk_levels):
    rows, cols = len(risk_levels) * 5, len(risk_levels[0]) * 5

    # A* search
    open = PriorityQueue([Node(start, None, 0, compute_h(start, end))])
    closed = set()

    while open.get_lowest_priority().position != end and open:
        current = open.pop_lowest_priority()
        closed.add(current.position)
        for direction in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            x, y = current.position
            x_adj = x + direction[0]
            y_adj = y + direction[1]
            if x_adj < 0 or cols <= x_adj or y_adj < 0 or rows <= y_adj:
                continue
            neighbour = (x_adj, y_adj)
            cost = current.g + compute_movement_cost_part_2(neighbour, risk_levels)
            if neighbour in open:
                if cost < open.get_by_position(neighbour).g:
                    open.remove_by_position(neighbour)
            if neighbour not in open and neighbour not in closed:
                neighbour_node = Node(neighbour, current, cost, compute_h(neighbour, end))
                open.append(neighbour_node)

    node = open.get_lowest_priority()
    return node.g



def part_one():
    logger.info(title)
    logger.info("--- Part One ---")
    print("--- Part One ---")

    start = (0, 0)
    end = (len(risk_levels) - 1, len(risk_levels[0]) - 1)
    total_risk_level_of_lowest_risk_path = search(start, end, risk_levels)
    print(total_risk_level_of_lowest_risk_path)

    logger.info("")


def part_two():
    logger.info(title)
    logger.info("--- Part Two ---")
    print("--- Part Two ---")

    start = (0, 0)
    end = ((len(risk_levels) * 5) - 1, (len(risk_levels[0]) * 5) - 1)
    total_risk_level_of_lowest_risk_path = search_part_2(start, end, risk_levels)
    print(total_risk_level_of_lowest_risk_path)
    logger.info("")


if __name__ == '__main__':
    print(title)

    risk_levels = None
    with(open("puzzle_input.txt", 'r')) as f:
        risk_levels = parse_input(f)

    part_one()
    part_two()

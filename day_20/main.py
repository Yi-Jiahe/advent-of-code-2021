import math

from aoc_logging import logger


title = ""


def parse_input(iterable):
    image_enhancement_algorithm =  None
    light_pixels = set()

    row = 0
    section = "image enhancement algorithm"
    for line in map(lambda line: line.strip(), iterable):
        match section:
            case "image enhancement algorithm":
                if line == "":
                    section = "input image"
                    continue
                image_enhancement_algorithm = line
            case "input image":
                for i, char in enumerate(line):
                    if char == '#':
                        light_pixels.add((i, row))
                row += 1
    return image_enhancement_algorithm, light_pixels


def find_image_boundaries(light_pixels):
    x_min, x_max = math.inf, -math.inf
    y_min, y_max = math.inf, -math.inf
    for x, y in light_pixels:
        x_min = min(x, x_min)
        x_max = max(x, x_max)
        y_min = min(y, y_min)
        y_max = max(y, y_max)
    return x_min, x_max, y_min, y_max


def enhance_image(image_enhancement_algorithm, light_pixels, n):
    new_light_pixels = set()

    x_min, x_max, y_min, y_max = find_image_boundaries(light_pixels)
    for x in range(x_min-1, x_max + 2):
        for y in range(y_min-1, y_max + 2):
            index_binary = ""
            for y_diff in [-1, 0, 1]:
                for x_diff in [-1, 0, 1]:
                    pixel = (x + x_diff, y + y_diff)
                    if image_enhancement_algorithm[0] == '#':
                        if n % 2 == 0:
                            if pixel[0] <= x_min - 1 or pixel[0] >= x_max + 1 or pixel[1] <= y_min -1 or pixel[1] >= y_max + 1:
                                index_binary += '1'
                                continue
                    index_binary += '1' if pixel in light_pixels else '0'
            index = int(index_binary, 2)
            if image_enhancement_algorithm[index] == '#':
                new_light_pixels.add((x, y))
    return new_light_pixels


def print_image(light_pixels):
    x_min, x_max, y_min, y_max = find_image_boundaries(light_pixels)
    for y in range(y_min, y_max + 1):
        row = ""
        for x in range(x_min, x_max + 1):
            row += '#' if (x, y) in light_pixels else '.'
        print(row)

def part_one():
    logger.info(title)
    logger.info("--- Part One ---")
    print("--- Part One ---")

    l = {pixel for pixel in light_pixels}
    for i in range(2):
        l = enhance_image(image_enhancement_algorithm, l, i+1)

    print(len(l))

    logger.info("")


def part_two():
    logger.info(title)
    logger.info("--- Part Two ---")
    print("--- Part Two ---")

    l = {pixel for pixel in light_pixels}
    for i in range(50):
        l = enhance_image(image_enhancement_algorithm, l, i+1)
    print(len(l))

    logger.info("")


if __name__ == '__main__':
    print(title)

    image_enhancement_algorithm, light_pixels = None, None
    with(open("puzzle_input.txt", 'r')) as f:
        image_enhancement_algorithm, light_pixels = parse_input(f)

    print(find_image_boundaries(light_pixels))

    part_one()
    part_two()

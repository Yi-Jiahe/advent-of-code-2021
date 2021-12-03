def part_1():
    print("--- Part One ---")

    horizontal_position, depth = 0, 0

    with open("planned_course.txt", 'r') as f:
        for line in f:
            command, units = line.strip().split(" ")
            units = int(units)
            match command:
                case "forward":
                    horizontal_position += units
                case "up":
                    depth -= units
                case "down":
                    depth += units
        print(f"Final horizontal position: {horizontal_position}")
        print(f"Final depth: {depth}")

        print(f"Answer {horizontal_position * depth}")


def part_2():
    print("--- Part Two ---")

    horizontal_position, depth, aim = 0, 0, 0

    with open("planned_course.txt", 'r') as f:
        for line in f:
            command, units = line.strip().split(" ")
            units = int(units)
            match command:
                case "forward":
                    horizontal_position += units
                    depth += aim * units
                case "up":
                    aim -= units
                case "down":
                    aim += units
    print(f"Final horizontal position: {horizontal_position}")
    print(f"Final depth: {depth}")

    print(f"Answer {horizontal_position * depth}")


if __name__ == '__main__':
    part_1()
    part_2()


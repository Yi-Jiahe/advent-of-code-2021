from aoc_logging import logger

title = "--- Day 16: Packet Decoder ---"


def parse_input(iterable):
    for line in map(lambda line: line.strip(), iterable):
        return line


def to_binary(hex_char):
    return bin(int(hex_char, 16))[2:].zfill(4)


def convert_transmission_to_binary(transmission):
    binary_transmission = ""
    for char in transmission:
        binary_transmission += to_binary(char)
    return binary_transmission


class Decoder:
    def __init__(self, transmission):
        self.binary_transmission = convert_transmission_to_binary(transmission)
        self.i = 0

        self.part_1_answer = 0

    def read_literal_value(self, start):
        value_binary = ""

        i = start
        while True:
            group = self.binary_transmission[i:i + 5]
            value_binary += group[1:5]
            i += 5

            if group[0] == '0':
                value = int(value_binary, 2)
                return i, value

    def read_packet(self, start):
        i = start

        packet_version_binary = self.binary_transmission[i:i + 3]
        packet_version = int(packet_version_binary, 2)
        i += 3

        packet_type_id_binary = self.binary_transmission[i:i + 3]
        packet_type_id = int(packet_type_id_binary, 2)
        i += 3


        if packet_type_id == 4:
            logger.info(f"{start}: Literal Value (version {packet_version})")
            i, value = self.read_literal_value(i)
            self.part_1_answer += packet_version
            return i, value

        logger.info(f"{start}: Operator packet (version {packet_version})")

        mode = self.binary_transmission[i]
        i += 1

        values = []
        match mode:
            case '0':
                total_length_of_subpackets = int(self.binary_transmission[i:i + 15], 2)
                i += 15

                end_of_subpackets = i + total_length_of_subpackets
                while i < end_of_subpackets:
                    i, value = self.read_packet(i)
                    values.append(value)
            case '1':
                total_subpackets = int(self.binary_transmission[i:i + 11], 2)
                i += 11

                subpackets_read = 0
                while subpackets_read < total_subpackets:
                    i, value = self.read_packet(i)
                    values.append(value)
                    subpackets_read += 1

        self.part_1_answer += packet_version

        match packet_type_id:
            case 0:
                return i, sum(values)
            case 1:
                value = 1
                for v in values:
                    value *= v
                return i, value
            case 2:
                return i, min(values)
            case 3:
                return i, max(values)
            case 5:
                return i, 1 if values[0] > values[1] else 0
            case 6:
                return i, 1 if values[0] < values[1] else 0
            case 7:
                return i, 1 if values[0] == values[1] else 0

    def parse_binary_transmission(self):
        _, value = self.read_packet(0)
        return value


def part_one(part_1_answer):
    logger.info(title)
    logger.info("--- Part One ---")
    print("--- Part One ---")

    print(f"Answer: {part_1_answer}")

    logger.info("")


def part_two(value):
    logger.info(title)
    logger.info("--- Part Two ---")
    print("--- Part Two ---")

    print(f"Value: {value}")

    logger.info("")


if __name__ == '__main__':
    print(title)

    transmission = None
    with(open("puzzle_input.txt", 'r')) as f:
        transmission = parse_input(f)

    decoder = Decoder(transmission)
    value = decoder.parse_binary_transmission()

    part_one(decoder.part_1_answer)
    part_two(value)

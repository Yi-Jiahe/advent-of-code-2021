import logging


def part_1(logger=logging):
    print("--- Part One ---")

    n_increases = 0

    with open("sonar_sweep_report.txt", 'r') as f:
        last_depth = None

        for line in f:
            depth = int(line.strip())

            if last_depth is None:
                logger.info(f"{depth} (N/A - no previous measurement)")
            else:
                if depth > last_depth:
                    n_increases += 1
                    logger.info(f"{depth} (increased), {n_increases}")
                elif depth < last_depth:
                    logger.info(f"{depth} (decreased)")
                else:
                    logger.info(f"{depth} (no change)")

            last_depth = depth

        print(f"{n_increases} measurements are larger than the previous measurement")


def part_2(logger=logging):
    print("--- Part Two ---")

    n_increases = 0

    window = []
    window_sum = 0
    last_window_sum = None

    with open("sonar_sweep_report.txt", 'r') as f:
        for line in f:
            depth = int(line.strip())

            window.append(depth)
            window_sum += depth

            if len(window) > 3:
                oldest_measurement = window.pop(0)
                window_sum -= oldest_measurement

            if len(window) == 3:
                if last_window_sum is None:
                    logger.info(f"{window_sum} (N/A - no previous sum)")
                else:
                    if window_sum > last_window_sum:
                        n_increases += 1
                        logger.info(f"{window_sum} (increased), {n_increases}")
                    elif window_sum < last_window_sum:
                        logger.info(f"{window_sum} (decreased)")
                    else:
                        logger.info(f"{window_sum} (no change)")

                last_window_sum = window_sum

    print(f"{n_increases} sums are larger than the previous sum")


if __name__ == '__main__':
    logger = logging.getLogger("Info Logger")
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler("info.log")
    logger.addHandler(handler)

    logger.info("Running Part One")
    part_1(logger)

    logger.info("Running Part Two")
    part_2(logger)
import numpy as np

if __name__ == '__main__':
    with open("diagnostic report.txt", 'r') as f:
        N_BITS = None

        # Part One
        counts = None
        for i, line in enumerate(f):
            number = line.strip()

            if i == 0:
                N_BITS = len(number)
                counts = np.zeros(N_BITS, dtype=int)
                # print(number, bits)

            for j, bit in enumerate(number):
                counts[j] += int(bit)

        print(f"Counts: {counts}")
        half = int(np.ceil(i/2))
        print(f"There are {i} numbers in the diagnostic report, majority is {half}")

        gamma_rate = 0
        epsilon_rate = 0
        for n, count in enumerate(counts[::-1]):
            value = np.power(2, n)
            # print(n, value)
            # print(count, half)
            if count > half:
                gamma_rate += value
            else:
                epsilon_rate += value
        print(f"Gamma rate   : {format(gamma_rate, f'0{N_BITS}b')} {gamma_rate}")
        print(f"Epsilion rate: {format(epsilon_rate, f'0{N_BITS}b')} {epsilon_rate}")

        power_consumption = gamma_rate * epsilon_rate

        print(f"The power consumption of the submarine is {power_consumption}")

        # Part Two
        oxygen_numbers = []
        co2_numbers = []
        majority = 1 if counts[0] > half else 0

        f.seek(0)
        for line in f:
            number = line.strip()
            if int(number[0]) == majority:
                oxygen_numbers.append(number)
            else:
                co2_numbers.append(number)

        # print(oxygen_numbers, co2_numbers)

        j = 1
        while len(oxygen_numbers) > 1 and j < N_BITS:
            new_oxygen_numbers = []
            count = 0
            for i, number in enumerate(oxygen_numbers):
                count += int(number[j])
            bit_criteria = 1 if count >= int(np.ceil(i/2)) else 0
            for number in oxygen_numbers:
                if int(number[j]) == bit_criteria:
                    new_oxygen_numbers.append(number)
            oxygen_numbers = new_oxygen_numbers
            j += 1
        oxygen_generator_rating = int(oxygen_numbers[0], 2)
        print(oxygen_numbers[0])
        print(format(oxygen_generator_rating, '012b'), oxygen_generator_rating)

        j = 1
        while len(co2_numbers) > 1 and j < N_BITS:
            new_co2_numbers = []
            count = 0
            for i, number in enumerate(co2_numbers):
                count += int(number[j])
            bit_criteria = 0 if count >= int(np.ceil(i/2)) else 1
            for number in co2_numbers:
                if int(number[j]) == bit_criteria:
                    new_co2_numbers.append(number)
            co2_numbers = new_co2_numbers
            j += 1
        co2_scrubber_rating = int(new_co2_numbers[0], 2)
        print(co2_scrubber_rating)

        life_support_rating = oxygen_generator_rating * co2_scrubber_rating
        print(f"The life support rating of the submarine is {life_support_rating}")
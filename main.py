from itertools import product


def create_number_combinations(n):
    if n <= 0:
        return []

    digits = [str(i) for i in range(10)]
    number_combinations = product(digits, repeat=n)
    sorted_number_combinations = [''.join(combination) for combination in number_combinations]
    return sorted_number_combinations


def write_numbers_in_file(combinations, filename):
    with open(filename, "w") as f:
        f.write('\n'.join(combinations))


file_name = input("Create new txt file with name: ")

try:
    n = int(input("Enter n: "))
    if n <= 0:
        print("Enter a positive integer!")

    else:
        numbers = create_number_combinations(n)
        write_numbers_in_file(numbers, file_name + ".txt")
        print(f"{file_name}.txt with {len(numbers)} {n}-digit combinations was created!")

except ValueError:
    print("Enter valid integer!")

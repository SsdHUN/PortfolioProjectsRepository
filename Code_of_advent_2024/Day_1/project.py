def process_file(file_path):
    first_column = []
    second_column = []

    with open(file_path, "r") as data:
        for line in data:
            number = line.strip().split()
            first_column.append(int(number[0]))
            second_column.append(int(number[1]))
    return first_column, second_column

if __name__ == "__main__":
    print(process_file("data.json"))
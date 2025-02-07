def process_file(file_path):
    first_column = []
    second_column = []

    with open(file_path, "r") as data:
        for line in data:
            number = line.strip().split()
            first_column.append(int(number[0]))
            second_column.append(int(number[1]))
    return first_column, second_column

def count_distance():
    distance = 0
    first_lsit , second_list = process_file("data.json")
    first_lsit.sort()
    second_list.sort()
    for i in range(len(first_lsit)):
        distance += abs(first_lsit[i] - second_list[i])
    return distance


def count_similarity_score():
    score = 0
    first_lsit , second_list = process_file("data.json")
    for number in first_lsit:
        count = second_list.count(number)
        score += number * count
    return score


if __name__ == "__main__":
    print(f'first task: {count_distance()}')
    print(f'second task: {count_similarity_score()}')
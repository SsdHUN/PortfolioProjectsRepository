

def open_file(file_path):
    with open(file_path, "r") as data:
        for line in data:
            print(line)

if __name__ == "__main__":
    open_file("data.json")
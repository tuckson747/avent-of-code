def main_part_1(data: list)->int:
    split = 0
    new_data = []
    for i in range(len(data)):
        inter = []
        for j in range(len(data[i])):
            inter.append(data[i][j])
        new_data.append(inter)
    for i in range(len(new_data)):
        if i == 0:
            index_S = new_data[i].index("S")
            new_data[i +1][index_S] = "|"
        else:
            for j in range(len(new_data[i])):
                if new_data[i][j] == "^":
                    if new_data[i-1][j] == "|":
                        split += 1
                        new_data[i][j - 1] = "|"
                        new_data[i][j + 1] = "|"

                elif new_data[i - 1][j] == "|":
                    new_data[i][j] = "|"
    return split

def main_part_2(data: list)->int:
    pass


if __name__ == "__main__":
    with open("input_day_7") as file:
        data = [line.strip() for line in file]
    for i in range(len(data)):
        data[i] = data[i].replace('\n', '')
    ans = main_part_1(data)
    print(ans)

    ans = main_part_2(data)
    print(ans)

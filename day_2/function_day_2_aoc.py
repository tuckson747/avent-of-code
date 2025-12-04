def main_part_1(inputs: list)->int:
    output = []
    for input in inputs:
        start,end = input.split("-")
        for i in range(int(start),int(end)+1):
            if len(str(i))%2 == 0:
                first_part = str(i)[:int(len(str(i))/2)]
                last_part = str(i)[int(len(str(i)) / 2):]
                if first_part == last_part:
                    output.append(i)
    return sum(output)


def main_part_2(inputs: list)->int:
    output = []
    for input in inputs:
        start, end = input.split("-")
        for i in range(int(start), int(end) + 1):
            for j in range(int(len(str(i))/2)):
                test = str(i)[:(j+1)]
                count = str(i).count(test)
                if count * (j+1) == len(str(i)):
                    output.append(i)
                    break

    return sum(output)


if __name__ == "__main__":
    with open("input_day_2.txt") as file:
        data = file.readline().split(",")

    ans = main_part_1(data)
    print(ans)

    ans = main_part_2(data)
    print(ans)

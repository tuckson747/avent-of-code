def main_part_1(data: list)->int:
    inputs = [[] for i in range(len(data[0].split(" ")))]
    for ligne in data:
        for i, num in enumerate(ligne.split()):
            inputs[i].append(num)
    output = []
    for problem in inputs:
        if len(problem) > 0:
            if problem[-1] == "+":
                output.append(sum([int(val) for val in problem[:-1]]))
            else:
                res = 1
                for val in problem[:-1]:
                    res *= int(val)
                output.append(res)

    return sum(output)


def main_part_2(data: list)->int:
    inputs = [[] for i in range(len(data[0].split(" ")))]
    iter = 0
    for i in range(len(data[0])):
        col = ""
        for j in range(len(data)-1):
            col += data[j][i]
        if len(list(set(col))) == 1 and col[0] == " " :
            iter += 1
        else:
            inputs[iter].append(col)
            col = ""
    iter = 0
    for elem in data[-1]:
        if elem != " ":
            inputs[iter].append(elem)
            iter += 1
    output = []
    for problem in inputs:
        if len(problem) > 0:
            if problem[-1] == "+":
                output.append(sum([int(val) for val in problem[:-1]]))
            else:
                res = 1
                for val in problem[:-1]:
                    res *= int(val)
                output.append(res)

    return sum(output)


if __name__ == "__main__":
    with open("input_day_6") as file:
        data = file.readlines()
    for i in range(len(data)):
        data[i] = data[i].replace('\n', '')
    ans = main_part_1(data)
    print(ans)

    ans = main_part_2(data)
    print(ans)
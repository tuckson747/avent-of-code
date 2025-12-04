def main_part_1(inputs: list)->int:
    output = 0
    directions = [(-1, -1), (-1, 0), (-1, 1),(0, -1), (0, 1),(1, -1), (1, 0), (1, 1)]
    for i in range(len(inputs)):
        for j in range(len(inputs[i])):
            if inputs[i][j] == '@':
                count = 0
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x <= len(inputs)-1 and 0 <= y <= len(inputs[i])-1 and inputs[x][y] == '@':
                        count += 1
                if count < 4:

                    output +=1
    return output


def main_part_2(inputs: list)->int:
    output = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    new_moved = 1
    while new_moved != 0:
        print(new_moved)
        new_moved = 0
        position_removed = []
        for i in range(len(inputs)):
            for j in range(len(inputs[i])):
                if inputs[i][j] == '@':
                    count = 0
                    for dx, dy in directions:
                        x, y = i + dx, j + dy
                        if 0 <= x <= len(inputs) - 1 and 0 <= y <= len(inputs[i]) - 1 and inputs[x][y] == '@':
                            count += 1
                    if count < 4:
                        position_removed.append((i,j))
                        new_moved += 1
                        output += 1
        for x,y in position_removed:
            lst = list(inputs[x])
            lst[y] = "."
            inputs[x] = "".join(lst)
    return output


if __name__ == "__main__":
    with open("input_day_4.txt") as file:
        data = [line.strip() for line in file]

    """ans = main_part_1(data)
    print(ans)"""

    ans = main_part_2(data)
    print(ans)

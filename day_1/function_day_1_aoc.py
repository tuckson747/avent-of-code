def main_part_1(inputs: list)->int:
    dial_pose = 50
    output = 0
    for seq in inputs:
        move = seq[0]
        click = int(seq[1:])%100
        if move == "L":
            dial_pose -= click
            tour = abs(dial_pose) // 100
            dial_pose += (tour * 100)
        else:
            dial_pose += click
            tour = abs(dial_pose) // 100
            dial_pose -= (tour * 100)
        if dial_pose == 0:
            output += 1

    return output



def main_part_2(inputs: list)->int:
    dial_pose = 50
    output = 0
    for seq in inputs:
        move = seq[0]
        clicks = int(seq[1:])
        if move == "L":
            for i in range(1,clicks+1):
                dial_pose -= 1
                if dial_pose == 0:
                    output += 1
                if dial_pose == -1:
                    dial_pose = 99

        else:
            for i in range(1, clicks + 1):
                dial_pose += 1
                if dial_pose == 100:
                    dial_pose = 0
                    output += 1

    return output


if __name__ == "__main__":
    with open("input_day_1.txt") as file:
        data = [line.strip() for line in file]

    ans = main_part_1(data)
    print(ans)

    ans = main_part_2(data)
    print(ans)
def main_part_1(inputs: list)->int:
    output = []
    for bank in inputs:
        new_bank = [int(val) for val in bank]
        first_digit = sorted(new_bank[:-1])[-1]
        second_digit = sorted(new_bank[(new_bank.index(first_digit)+1):])[-1]
        output.append(int(f"{first_digit}{second_digit}"))
    return sum(output)


def main_part_2(inputs: list)->int:
    total = 0
    for bank in inputs:
        stack = []
        to_remove = len(bank) - 12
        for ch in bank:
            while to_remove > 0 and stack and stack[-1] < ch:
                stack.pop()
                to_remove -= 1
            stack.append(ch)

        total += int(''.join(stack[:12]))

    return total


if __name__ == "__main__":
    with open("input_day_3.txt") as file:
        data = [line.strip() for line in file]

    """ans = main_part_1(data)
    print(ans)"""

    ans = main_part_2(data)
    print(ans)

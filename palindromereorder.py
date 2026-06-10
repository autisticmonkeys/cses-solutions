from collections import Counter

string = input()
counter = Counter(string)

odd_chars = [char for char, count in counter.items() if count % 2 == 1]

if len(odd_chars) > 1:
    print("NO SOLUTION")
else:
    left_half = []
    middle = ""

    if len(odd_chars) == 1:
        middle = odd_chars[0]
        counter[middle] -= 1

    for char, count in counter.items():
        left_half.append(char * (count // 2))

    left_str = "".join(left_half)

    print(left_str + middle + left_str[::-1])

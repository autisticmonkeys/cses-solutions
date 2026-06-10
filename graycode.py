n = int(input())

for i in range(1 << n): # 1 << n means 2 to the power of n, basically run the loop 2^n times
    print(format(i ^ (i >> 1), f"0{n}b"))  # format means the way in which the value is displayed,  f"0{n}b" means
    # f means f string, 0 means to pad with zeroes, or fill the remaining spaces with zeroes from the left as
    # 0 comes to the left of n, {n} means that the width of the output will be n
    # b means to display the numbar in binary format
    # i ^ (i >> 1) XORs i with i right shifted by 1, which the gray code formula

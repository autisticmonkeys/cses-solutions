# this program takes an integer n as input
# if n is even, it divides it by 2, if it's odd, it multiplies it by 3 and adds 1, until the 4 2 1 cycle is reached
num = int(input(""))
print(num, end=" ")
while num != 1:
    if num%2 == 0:
        num = num//2
    else:
        num = (num*3)+1
    print(num, end=" ")
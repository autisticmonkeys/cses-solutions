# this program finds the longest single chain in a dna sequence
dna = str(input(""))
dna_arr = list(dna)
i = 0
# convert the string into an array, and then increase temp, as the chains get continuous
# when chain breaks, max = temp, and temp = 0
# temp starts counting again, and keeps checking against max, if temp > max, then max = temp
n = len(dna)
temp = 1
max1 = 1
while i <= n-2:
    if dna_arr[i + 1] == dna_arr[i]:
        temp += 1
    else:
        temp = 1
    if temp > max1:
        max1 = temp
    i += 1
print(max1)
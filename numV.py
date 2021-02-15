#print how many vowels occur in string

s = 'azcbobobegghakl'
numV = 0

for char in s:
    if char == 'o' or char == 'e' or char == 'i' or char == 'a' or char == 'u':
        numV += 1
        # print(char)

print('Number of vowels is: ' + str(numV))

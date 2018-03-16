#!/usr/bin/python
import re
'''block of getting n and m'''

print("Getting integers n and m:")
input_string = input()
n = 0
m = 0
result = re.search(r'(\d{1,4}|10000) (\d{1,2}|100)', input_string)
if result:
    print("good input string!")
    n = re.findall(r'\d+', input_string)
else:
    print("Bad input string!")
    exit()

'''block of getting n and m'''
listA = []
listB = []

print("put words of group A:")
for i in range(int(n[0])):
    # global listA
    word = input()
    listA.append(word)

print("put words of group B:")
for y in range(int(n[1])):
    # global listB
    word = input()
    listB.append(str(word))


c = {}
for g in range(len(listB)):
        for i in range(len(listA)):
                # global listA
                # global listB
                # global c
                if listA[i] == listB[g]:
                        c[i] = str(listA[i])
keys = []
keys.append(list(c.keys()))
new_list = list(c.values())
jump = 0
i = 0
cycle = len(new_list)-1
old_string = c.values()
countB = 0
while i <= cycle:
    stop = 0
    jump = 0
    outPutString = str(keys[0][i] + 1) + " "
    for g in range(i + 1, len(new_list)):
        # global stop
        # global jump
        if new_list[i] != new_list[g]:
            stop = 1
        if stop == 0:
            jump += 1
        if new_list[i] == new_list[g]:
            outPutString += str(keys[0][g] + 1)
            outPutString += " "
    i += jump
    i += 1
    if countB < len(listB):
        countB += 1
    print(outPutString)

numberList = [1,4,5,2,3,10,9,6]

print(numberList)

min = numberList[0]

n = len(numberList)
for i in range(0, n-1):
    for j in range(i, n):
        if numberList[j]<numberList[i]:
            temp = numberList[i]
            numberList[i] = numberList[j]
            numberList[j] = temp
print(numberList)
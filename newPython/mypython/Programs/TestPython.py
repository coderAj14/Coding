

firstList = [1,4,7,6,3,5,8,9,12,43,56,43,45,67]

secondList = [3, 34, 56,2,3,567,67,87,43,45]


newList = []
for number in firstList:
    if number in secondList:
        newList.append(number)

print newList
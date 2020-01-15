
input  =[4, 5, 2, 25]
#[7 ,2 ,8 ,4 ,10 ,11 ,9 ,5 ,12]

tempList = [input[len(input)-1]]
for number in input[len(input)-2::-1]:

    while len(tempList) > 0:
        element = tempList.pop()
        if number < element:
            tempList.append(element)
            tempList.append(number)
            print "number is {num} greater element is {ele} ".format(num =number, ele = element)
            break






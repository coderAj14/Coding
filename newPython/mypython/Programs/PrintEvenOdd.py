import os

class PrintEvenOdd(object):

    def __init__(self):
        pass

    def printNumberType(self, number):
        self.number = number
        print self.number

        if self.number % 2 == 0:
            print('number is even')
        else:
            print('number is odd')

    def printRange(self, a, b):
        print (range(a, b))

    def ListFilesInCurrentDir(self):
        for root, dir, files in os.walk("."):
            for fileNames in files :
                print fileNames

    def printAge(self):
        name =raw_input('enter your name ')
        age = raw_input('enter your age')
        print "Hi %s your age is %s. have a good day \n" % (name,age)
        print "Hi %s your age is %s. have a good day \n" % (name,age)


    def listFunctions(self):
        tempList = [1,2,3,4,5,6,7,8,9]
        newList =  [number for number in tempList if number <5]
        print newList





sampleObject = PrintEvenOdd()

sampleObject.listFunctions()
sampleObject.printNumberType(6)

sampleObject.printNumberType(7)


sampleObject.printRange(4,20)

sampleObject.ListFilesInCurrentDir();

#sampleObject.printAge();
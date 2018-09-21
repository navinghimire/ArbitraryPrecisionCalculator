__author__ = "Navin Ghimire"
__email__ = "nghimire@uh.edu"
__version__ = "1.0.0"
from enum import Enum
import re
class Node:
    carry = 0
    value = []
    def __init__(self,value):
        self.value = value
    def addToList(self,num):
        self.value.insert(0,num)
    def __str__(self):
        print(self.carry,self.value)

    def __str__(self):
        return str(self.carry) + str(self.value)
class OperatorType(Enum):
    ADD = "+"
    MULTIPLY = "*"
class Expression:
    operator = OperatorType
    operand1 = 0
    operand2 = 0
    def __init__(self,operand1,operator,operand2):
        self.operand1 = operand1
        self.operator = operator
        self.operand2 = operand2


def addNodesRecursively(node1, node2, result, counter, carryToAdd):
    if counter == 0:
        return 0
    sum = addNodesRecursively(node1, node2, result, counter-1, carryToAdd) + node1.value[len(node1.value)-counter] + node2.value[len(node2.value)-counter] + (carryToAdd if counter == 1 else 0)
    result.addToList(sum % 10)
    return sum//10

def addListRecursively(list1, list2, result, lcounter):
    if lcounter == 0:
        return 0
    addListRecursively(list1, list2, result, lcounter - 1)
    resu = Node([])
    myCarry = 0
    if len(result) > 0:
        myCarry = result[0].carry
    resu.carry = addNodesRecursively(list1[len(list1)-lcounter],list2[len(list2)-lcounter],resu,len(list1[0].value), myCarry)
    result.insert(0, resu)
    return resu.carry

def processFile(file):
    line = file.readline()
    if line.strip() == '':
        return
    if line.find("*") != -1:
        line = line.rstrip().split("*")
        Expression(line[0],line[1],OperatorType.MULTIPLY)
    elif line.find("+") != -1:
        line = line.rstrip().split("+")
        Expression(line[0], line[1], OperatorType.ADD)
    print(line)
    processFile(file)


def main():

    dpn = 2

    f = open('m', "r")
    processFile(f)
    f.close()


    a = "999999999999999999999"
    b = "1"
    if len(a) > len(b):
        c = len(a)-len(b)
        b = c*'0'+b
    elif len(a) < len(b):
        c = len(b)-len(a)
        a = c*'0'+a
    if len(a) % dpn != 0:
        c = dpn - len(a)%dpn
        a = c*'0'+a
        b = c*'0'+b
        print(c)
    print(b)
    cc = len(a)%dpn
    mylist = re.findall(dpn*'.',a[cc:])
    mylist2 = re.findall(dpn*'.',b[cc:])
    mylist = [Node(list(map(int,l))) for l in mylist]
    mylist2 = [Node(list(map(int, l))) for l in mylist2]
    [print(l.value,end=" ") for l in mylist]
    print()
    [print(l.value,end=" ") for l in mylist2]
    result = []
    print()
    addListRecursively(mylist, mylist2, result, len(mylist2))
    print("here we go")
    a = str(result[0].carry)
    for node in result:
        for l in node.value:
            a = a+ str(l)
    print(a.lstrip('0'))

if __name__ == "__main__":
    main()

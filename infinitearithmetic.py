__author__ = "Navin Ghimire"
__email__ = "nghimire@uh.edu"
__version__ = "1.0.0"
import re
import sys
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
class Expression:
    operator = ''
    operand1 = 0
    operand2 = 0
    def __init__(self,operand1,operand2,operator):
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

def multiply(listNode1,listNode2,dpn,counter):
    if counter == 0:
        return '0'
    rightPadding = len(listNode2)-counter
    return add(addTimes(listNode1,int(listNode2[counter-1]),dpn)+ rightPadding*'0',multiply(listNode1,listNode2,dpn,counter-1),dpn)

#add a given node this many times recursively
def addTimes(listNodes,times,dpn):
    if times == 0:
        return "0"
    return add(addTimes(listNodes,times-1,dpn),listNodes,dpn)

# given two string of digits, add them and return a result string
def add(aString,bString,dpn):
    r = []
    pv = alignOperands([aString, bString], dpn)
    pv = convertToNode(pv,dpn)
    addListRecursively(pv[0], pv[1], r, len(pv[0]))
    resultString = extractResult(r)
    return resultString

def processFile(file,dpn):
    line = file.readline()
    if line.strip() == '':
        return
    if line.find("*") != -1:
        line = line.rstrip().split("*")
        line = Expression(line[0],line[1],'*')
        a = alignOperands([line.operand1, line.operand2], dpn)
        resultString = multiply(a[0], a[1], dpn, len(a[1]))

    elif line.find("+") != -1:
        line = line.rstrip().split("+")
        line = Expression(line[0], line[1], '+')
        resultString = add(line.operand1,line.operand2,dpn)

    print("%s%s%s=%s" % (line.operand1,line.operator,line.operand2,resultString))

    processFile(file,dpn)

def alignOperands(li,dpn):
    a = li[0]
    b = li[1]
    if len(a) > len(b):
        c = len(a) - len(b)
        b = c * '0' + b
    elif len(a) < len(b):
        c = len(b) - len(a)
        a = c * '0' + a
    if len(a) % dpn != 0:
        c = dpn - len(a) % dpn
        a = c * '0' + a
        b = c * '0' + b
        #print(c)
    #print(b)
    return [a,b]

def convertToNode(li,dpn):
    a = li[0]
    b = li[1]
    cc = len(a) % dpn
    operand1List = re.findall(dpn * '.', a[cc:])
    operand2List = re.findall(dpn * '.', b[cc:])
    operand1List = [Node(list(map(int, l))) for l in operand1List]
    operand2List = [Node(list(map(int, l))) for l in operand2List]
    return[operand1List,operand2List]

def printNodes(kk, counter):
    if (counter == 0):
        return ''
    return str(kk.value[len(kk.value)-counter]) + printNodes(kk,  counter - 1)

def printListNodes(result, counter):
    if (counter == 0):
        return ''
    return printListNodes(result,counter-1)+printNodes(result[counter-1],len(result[counter-1].value))

def extractResult(result):
    a = str(result[0].carry)
    a = a+printListNodes(result,len(result))
    return (a.lstrip('0')) if a.lstrip('0') != '' else '0'

def main():
    # extracting command line argument- filename and digits per node (dpn)
    arguments = sys.argv[1].split(";")
    filename = arguments[0].split("=")[1]
    dpn = int(arguments[1].split("=")[1])

    #opening file for processing
    f = open(filename, "r")

    #recursive fuction to process each lines
    processFile(f,dpn)
    f.close()

if __name__ == "__main__":
    main()

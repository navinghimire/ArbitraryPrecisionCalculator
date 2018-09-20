__author__ = "Navin Ghimire"
__email__ = "nghimire@uh.edu"
__version__ = "1.0.0"

import re
class Node:
    carry = 0
    value = []
    def __init__(self,data):
        self.value = data
    def add(self,otherNode):
        return

    def print(self):
        print(self.carry,self.value)

#add two nodes
def add(node1,node2,resultNode,counter):
    if (counter == 0):
        return 0
    sum = add(node1,node2,resultNode,counter-1)+node1.value[counter-1]+node2.value[counter-1]
    resultNode.add(sum%10)
    return sum//10
def main():
    dpn = 3
    f = open('m',"r")
    lines = list(f)
    f.close()

    a = "78624567886546777633673"
    b = "53424572170987686547897"

    cc = len(a)%dpn

    mylist = re.findall(dpn*'.',a[cc:])
    mylist.insert(0,a[:cc])
    mylist2 = re.findall(dpn*'.',b[cc:])
    mylist2.insert(0, b[:cc])
    mylist = [Node(list(map(int,l))) for l in mylist]
    mylist2 = [Node(list(map(int, l))) for l in mylist2]
   # mylist[1].print()
    resultNode = Node(3)
    resultNode.carry = add(mylist[1],mylist[1],resultNode,3)
    resultNode.print()

if __name__ == "__main__":
    main()

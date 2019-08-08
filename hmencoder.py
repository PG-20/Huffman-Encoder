import sys

nodeList = []
codeMap = {}
frequencyMap = {}
stringList = []

def genCode(tree, code=""):
    if tree.left == None and tree.right == None:
        codeMap[tree.key] = code
        stringList.append(tree.key+": "+code+"\n")
        
    if tree.left:
        genCode(tree.left, code+"0")
    if tree.right:
        genCode(tree.right, code+"1")

def sort(l):
    l.sort(key = lambda x: (x.frequency, x.key))

class Node:
    def __init__(self, data, frequency=1, left=None, right=None):
        self.left = left
        self.right = right
        self.frequency = frequency
        self.key = data
    
    def increaseFrequency(self):
        self.frequency+=1

with open(sys.argv[1], 'r') as f:
    message = f.read()

for i in message:
	if i in frequencyMap:
		frequencyMap[i].increaseFrequency()
	else:
		frequencyMap[i]=Node(i)
	
nodeList = list(frequencyMap.values())

sort(nodeList)

while len(nodeList)>1:
    x = nodeList.pop(0)
    y = nodeList.pop(0)
    left = x if min(x.key,y.key)==x.key else y
    right = x if left==y else y
    newTree = Node(left.key+right.key, left.frequency+right.frequency, left, right)
    nodeList.append(newTree)
    sort(nodeList)

genCode(nodeList[0])

stringList.sort()
ave=0

with open('encodemsg.txt', 'w') as f:
    encoded=""
    for i in message:
        encoded+=codeMap[i]
    ave = float(len(encoded))/len(message)
    for i in range((len(encoded)//80)+1):
        f.write(encoded[(i*80):(i*80)+80]+"\n")

with open('code.txt', 'w') as f:
    for i in stringList:
        if i[0]==" ":
            i="Space"+i[1:]
        f.write(i)
    f.write("Ave = "+str(round(ave,2))+" bits per symbol")
    
        
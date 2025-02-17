memory = []
head, prev, curr = None, None, None
dataArray = [['호날두', '010-1111-1111'], ['메시', '010-2222-2222'], ['벨링엄', '010-3333-3333']]
# dataArray = [[input('이름, 연락처')]]
# print(dataArray)
class Node:
    def __init__(self, data):
        self.__data = data
        self.__link = None
    
    def getLink(self):
        return self.__link
    
    def setLink(self, link):
        self.__link = link

    def getData(self):
        return self.__data
    
    # def setData(self, data):
    #     self.__data = data

def printNode(start):
    curr = start
    if curr == None: return

    print(curr.getData(), end=' -> ')

    while curr.getLink() != None:
        curr = curr.getLink()
        if curr.getLink() == None:
            print(curr.getData(), end=' ')
        else:
            print(curr.getData(), end=' -> ')
        
    print()

def insertNode(foundData, insertData):
    global memory, head, curr, prev
    # print('check', head)
    if head.getData() == foundData:
        node = Node(insertData)
        node.setLink(head)
        head = node
        return
    
    curr = head
    while curr.getLink() != None:
        prev = curr
        curr = curr.getLink()
        if curr.getData() == foundData:
            node = Node(insertData)
            node.setLink(curr)
            prev.setLink(node)
            return
        
    node = Node(insertData)
    curr.setLink(node)

def deleteNode(dataToDelete):
    global memory, head, prev, curr

    if head.getData() == dataToDelete:
        curr = head
        head = head.getLink()
        del(curr)
        return
    
    curr = head
    while curr.getLink() != None:
        prev = curr
        curr = curr.getLink()
        if curr is None: return
        if curr.getData() == dataToDelete:
            prev.setLink(curr.getLink())
            del(curr)
            return
        
def findNode(foundData):
    global prev, curr, head, memory

    curr = head
    if curr.getData() == foundData:
        return curr
    while curr.getLink() != None:
        curr = curr.getLink()
        if curr.getData() == foundData:
            return curr
        
    return None

def run():
    global dataArray, head
    node = Node(dataArray[0])
    head = node
    # print('check', head)
    memory.append(node)

    for name in dataArray[1:]:
        prev = node
        node = Node(name)
        prev.setLink(node)
        memory.append(node)

    while True:
        inputNum = int(input('실행할 번호 입력 '))
        if inputNum == 1:
            originData = input('뒤의 데이터 ').split(',')
            dataToInsert = input('삽입할 데이터 ').split(',')
            insertNode(originData, dataToInsert)
            printNode(head)
        elif inputNum == 2:
            dataArray = input('이름').split(',')
            deleteNode(dataArray)
            printNode(head)
        elif inputNum == 3:
            printNode(head)
        else:
            return



if __name__ == '__main__':
    run()
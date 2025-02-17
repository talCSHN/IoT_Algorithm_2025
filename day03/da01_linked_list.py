# 단순 연결 리스트

# 전역변수
memory = [] # 컴퓨터 메모리처럼 보이게 만든 변수
head, prev, curr = None, None, None # 항상 첫번째 노드, curr 바로 앞의 노드, 현재 선택한 노드
dataArray = ['다현', '정연', '쯔위', '사나', '나연',]

class Node:
    def __init__(self, data):
        self.__data = data
        self.__link = None

    def setLink(self, link):
        self.__link = link

    def getData(self):
        return self.__data
    
    def getLink(self):
        return self.__link
    
    def __str__(self):
        return self.__data


def printNode(start):
    # global curr
    curr = start
    if curr == None: return

    print(curr.getData(), end=' -> ')
    
    while curr.getLink() != None:    # 현재링크의 다음링크가 있는 동안
        curr = curr.getLink()    # 다음 노드를 가리킴
        if curr.getLink() == None:
            print(curr.getData(), end=' ')  # 더 이상 다음 노드가 없으니 화살표 필요없음
        else:
            print(curr.getData(), end=' -> ')

    print() # 그냥 한 줄 내려줌

def insertNode(foundData, insertData):
    global memory, head, curr, prev # 전역변수 가져와서 insertNode메서드 안에서 쓰겠다는 선언

    # 맨 처음에 데이터 삽입
    if head.getData() == foundData:
        node = Node(insertData)
        node.setLink(head)  # 현재 head가 가리키는 node를 새 node의 link로 연결
        head = node # head는 새 node로 할당
        return  # 더이상 밑의 로직이  실행안되도록 함수 탈출

    # 중간에 데이터 삽입
    curr = head
    while curr.getLink() != None:
        prev = curr
        curr = curr.getLink()
        if curr.getData() == foundData:
            node = Node(insertData)
            node.setLink(curr)
            prev.setLink(node)
            return  # 더이상 밑의 로직이 실행안되도록 함수 탈출
    
    # 마지막에 데이터 삽입
    node = Node(insertData)
    curr.setLink(node)

def deleteNode(dataToDelete):
    global memory, head, prev, curr

    if head.getData() == dataToDelete:  # 첫번째 노드 삭제
        curr = head
        head = head.getLink()
        del(curr)
        return
    
    curr = head # 중간/마지막 노드 삭제
    while curr.getLink() != None:
        prev = curr
        curr = curr.getLink()
        if curr is None: return # 단순로직으로 예외처리
        if curr.getData() == dataToDelete:
            prev.setLink(curr.getLink())    # 지울 node의 링크를 prev에서 가리키도록
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
        
    return None # 찾는 데이터가 없음

# 연결리스트 생성, 삽입, 삭제 구현
if __name__ == '__main__':  # 시작 모듈일때
    node = Node(dataArray[0])
    head = node
    memory.append(node)

    for name in dataArray[1:]:  # 1번 인덱스 데이터('정연')부터 마지막 데이터('나연') 
        prev = node # 다현이 들어있는 노드를 prev에 할당
        node = Node(name)   # name=0 -> 정연, name=1 -> 쯔위, name=2 -> 사나, name=3 -> 나연
        prev.setLink(node)    # 이전 노드에 현재 노드를 연결
        memory.append(node)
    
    printNode(head)
    # 5개 데이터를 가지는 연결리스트 생성 완료

    # 데이터 삽입 구현
    insertNode('다현', '호날두')
    printNode(head)

    insertNode('사나', '메시')
    printNode(head)

    insertNode('', '벨링엄')
    printNode(head)

    # 데이터 검색
    foundNode = findNode('메시')
    print(foundNode)
    
    foundNode = findNode('펠레')
    print(foundNode)

    # 데이터 삭제
    deleteNode('호날두')
    printNode(head)

    deleteNode('메시')
    printNode(head)

    deleteNode('')
    printNode(head)

    deleteNode('벨링엄')
    printNode(head)

    

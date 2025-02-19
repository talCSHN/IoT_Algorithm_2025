from operator import itemgetter

G = None
nameArr = ['춘천', '서울', '속초', '대전', '광주', '부산']
춘천, 서울, 속초, 대전, 광주, 부산 = 0, 1, 2, 3, 4, 5
SIZE = len(nameArr)

class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def printGraph(g):
    global nameArr

    print('\t', end='')
    for v in range(g.SIZE):
        print(nameArr[v], end='\t')
    print()

    for row in range(g.SIZE):
        print(nameArr[row], end='\t')
        for col in range(g.SIZE):
            print(f'{g.graph[row][col]:4d}', end='\t')
        print()
    print()

def findVertex(g, foundVtx):
    stack = []
    visitedArr = []

    current = 0
    stack.append(current)
    visitedArr.append(current)

    while len(stack) != 0:
        next = None
        for vertex in range(SIZE):
            if g.graph[current][vertex] != 0:
                if vertex in visitedArr:
                    continue
                else:
                    next = vertex
                    break
        if next != None:
            current = next
            stack.append(current)
            visitedArr.append(current)
        else:
            current = stack.pop()

    if foundVtx in visitedArr:
        return True
    else:
        return False
    
G = Graph(SIZE)

G.graph[춘천][서울] = 10; G.graph[춘천][속초] = 15
G.graph[서울][춘천] = 10; G.graph[서울][속초] = 40; G.graph[서울][대전] = 11; G.graph[서울][광주] = 50
G.graph[속초][춘천] = 15; G.graph[속초][서울] = 40; G.graph[속초][대전] = 12
G.graph[대전][서울] = 11; G.graph[대전][속초] = 12; G.graph[대전][부산] = 30; G.graph[대전][광주] = 20
G.graph[광주][서울] = 50; G.graph[광주][대전] = 20; G.graph[광주][부산] = 25
G.graph[부산][대전] = 30; G.graph[부산][광주] = 25

print('###### 전체 연결도 #######')
printGraph(G)

edgeArr = []
for row in range(SIZE):
    for col in range(SIZE):
        if G.graph[row][col] != 0:
            edgeArr.append((G.graph[row][col], row, col))

print('## 간선 목록 -> ', end=' ')
print(edgeArr)

edgeArr= sorted(edgeArr, key=itemgetter(0), reverse=True)
print('## 간선목록 정렬 -> ', end=' ')
print(edgeArr)

newArr = []
for i in range(0, len(edgeArr), 2):
    newArr.append(edgeArr[i])

print('##### 중복간선 제거된 목록 ->', end=' ')
print(newArr)

index = 0
while len(newArr) > (SIZE - 1):
    start = newArr[index][1]
    end = newArr[index][2]
    saveWeight = newArr[index][0]

    G.graph[start][end] = 0
    G.graph[end][start] = 0

    startYN = findVertex(G, start)
    endYN = findVertex(G, end)

    if startYN and endYN:
        del(newArr[index])
    else:
        G.graph[start][end] = saveWeight
        G.graph[end][start] = saveWeight
        index += 1

print('## 최소비용 신장트리 결과')
printGraph(G)
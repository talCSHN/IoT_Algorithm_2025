# 최소비용신장트리
from operator import itemgetter # 튜플, 리스트의 인덱스에 해당하는 아이템을 가져올때 쓰는 모듈


# 전역변수
G = None
nameArr = ['춘천', '서울', '속초', '대전', '광주', '부산']
춘천, 서울, 속초, 대전, 광주, 부산 = 0, 1, 2, 3, 4, 5
SIZE = len(nameArr) # 6

# 클래스 선언
class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

# 개선된 그래프 출력
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

# 특정 정점에 그래프 연결 확인하는 함수
def findVertex(g, foundVtx):
    stack = []
    visitedArr = []

    current = 0 # 시작 정점
    stack.append(current)
    visitedArr.append(current)


    while len(stack) != 0:  # Stack의 길이가 0이 되면 모든 정점을 방문했다는 뜻
        next = None
        for vertex in range(SIZE):
            if g.graph[current][vertex] != 0:  # 간선이 있다
                if vertex in visitedArr:    # 도착점이 이미 방문했으면
                    continue
                else:
                    next = vertex   # 다음 번 방문할 정점
                    break
        if next != None:    # 다음에 방문할 정점이 있으면
            current = next
            stack.append(current)
            visitedArr.append(current)
        else:
            current = stack.pop()

    if foundVtx in visitedArr:
        return True
    else:
        return False
    
# 초기화
G = Graph(SIZE)

G.graph[춘천][서울] = 10; G.graph[춘천][속초] = 15
G.graph[서울][춘천] = 10; G.graph[서울][속초] = 40; G.graph[서울][대전] = 11; G.graph[서울][광주] = 50
G.graph[속초][춘천] = 15; G.graph[속초][서울] = 40; G.graph[속초][대전] = 12
G.graph[대전][서울] = 11; G.graph[대전][속초] = 12; G.graph[대전][부산] = 30; G.graph[대전][광주] = 20
G.graph[광주][서울] = 50; G.graph[광주][대전] = 20; G.graph[광주][부산] = 25
G.graph[부산][대전] = 30; G.graph[부산][광주] = 25

print('## 자전거 도로 전체 연결도 ##')
printGraph(G)

# 가중치 간선 목록
edgeArr = []
for row in range(SIZE):
    for col in range(SIZE):
        if G.graph[row][col] != 0:  # 가중치가 있음
            edgeArr.append((G.graph[row][col], row, col))

print('## 간선 목록 -> ', end=' ')
print(edgeArr)

# 가중치별 간선 내림차순 정렬
# itemgetter(0) -> (weight, slot, elot) 중 weight로 정렬하겠다
edgeArr = sorted(edgeArr, key=itemgetter(0), reverse=True)
print('## 간선목록 정렬 ->', end=' ')
print(edgeArr)

# 중복간선 제거
newArr = []
for i in range(0, len(edgeArr), 2):
    newArr.append(edgeArr[i])

print('## 중복간선 제거된 목록 ->', end=' ')
print(newArr)

# 가중치 높은 간선부터 제거
index = 0
# 0:춘천, 1:서울, 2:속초, 3:대전, 4:광주, 5:부산
while len(newArr) > (SIZE - 1): # 간선의 수가 (정점갯수 - 1) 될 때까지 반복
    start = newArr[index][1]    # 서울부터 시작
    end = newArr[index][2]  # 광주부터 시작
    saveWeight = newArr[index][0]   # 현재 가중치 저장(복원을 위해)

    G.graph[start][end] = 0 # 무조건 지움
    G.graph[end][start] = 0 # 무방향이라 양쪽으로 값이 다 있음

    startYN = findVertex(G, start)  # 서울에 연결된 간선 확인
    endYN = findVertex(G, end)  # 광주에 연결된 간선 확인

    if startYN and endYN:   # 둘 다 다른 간선 있으니까 지금 간선을 지워도 됨
        del(newArr[index])
    else:   # 연결된 간선이 없으니까 지웠던 인접행렬 값을 원상복귀
        G.graph[start][end] = saveWeight
        G.graph[end][start] = saveWeight
        index += 1
        
# 결과 출력
print('## 최소비용 신장트리 결과')
printGraph(G)
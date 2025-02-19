# 그래프 깊이 우선탐색

# stack = [] 리스트. append(push()와 동일), pop()으로 스택 구현 가능
# print(stack)
# stack.append(5)
# print(stack)
# stack.append(7)
# print(stack)
# data = stack.pop()
# print(stack)

# 전역 변수
stack = []  # 스택
visitedArr = []    # 방문기록


class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

# 메인코드
SIZE = 4
G1 = Graph(SIZE)
# 0:A, 1:B, 2:C, 3:D
G1.graph[0][2] = 1
G1.graph[0][3] = 1
G1.graph[1][2] = 1
G1.graph[2][0] = 1
G1.graph[2][1] = 1
G1.graph[2][3] = 1
G1.graph[3][0] = 1
G1.graph[3][2] = 1

print('## G1 무방향 그래프 ##')
for row in range(G1.SIZE):
    for col in range(G1.SIZE):
        print(G1.graph[row][col], end=' ')
    print()

print('## DFS 시작 ##')

current = 0 # A에서 시작
stack.append(current)   # Stack에 push(A)
visitedArr.append(current)  # 방문기록에 A 들어감


while len(stack) != 0:  # Stack의 길이가 0이 되면 모든 정점을 방문했다는 뜻
    next = None
    for vertex in range(SIZE):
        if G1.graph[current][vertex] == 1:  # 간선이 있다
            if vertex in visitedArr:    # 도착점에 이미 방문했으면
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


print('방문순서', end=' -> ')
for i in visitedArr:
    print(chr(ord('A') + i), end=' ') # A의 ASCII 코드값 출력

# print()
# print(chr(ord('A')+2)) # A의 ASCII 코드값 출력
# 이진 트리 구현


# 초기화
memory = []
root = None
nameArray = ['레알', '맨시티', '리버풀', '바르샤', '뮌헨', '맨유']

# TreeNode 클래스 선언
class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

# 메인 모듈
if __name__ == '__main__':
    node = TreeNode()
    node.data = nameArray[0]
    root = node
    memory.append(node)

    for name in nameArray[1:]:
        node = TreeNode()
        node.data = name

        current = root
        while True:
            if name < current.data: # 현재 name이 노드 안 데이터보다 작으면 왼쪽으로 보냄
                if current.left == None:
                    current.left = node
                    break   # 연결했으니까 반복문 탈출
                else:
                    current = current.left  # 왼쪽으로 더 내려감
            else:   # 오른쪽으로 보냄
                if current.right == None:
                    current.right = node
                    break
                else:
                    current = current.right

        memory.append(node)
    print('이진트리 탐색 구성완료')

    findName = input('찾을 이름 입력 > ')

    current = root  # 루트노드부터 검색 시작
    count = 0
    while True:
        if findName == current.data:
            print(f'{findName} 찾음')
            count += 1
            break
        elif findName < current.data:
            if current.left == None:
                print(f'{findName} 트리에 없음')
                break
            else:
                current = current.left
                count += 1
        else:
            if current.right == None:
                print(f'{findName} 트리에 없음')
                break
            else:
                current = current.right
                count += 1

    print(f'검색 종료. 총 검색 횟수:{count}')

    # 트리노드 삭제(리버풀, 바르샤 삭제)
    delName = input('삭제할 노드 입력 > ')

    current = root
    parent = None
    while True:
        if delName == current.data: # 삭제할 때

            if current.left == None and current.right == None:  # 리프노드
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
                del(current)
            elif current.left != None and current.right == None: # 왼쪽 노드에 자식이 있고, 오른쪽에는 없을때
                if parent.left == current:
                    parent.left = current.left
                else:
                    parent.right = current.left
                del(current)
            elif current.left == None and current.right != None: # 오른쪽 노드에 자식이 있고, 왼쪽에는 없을때
                if parent == None:
                    print('최상위 노드는 삭제 불가')
                    break
                elif parent.left == current:
                    parent.left = current.right
                else:
                    parent.right = current.right
                del(current)
            
            print(f'{delName} 삭제함')
            break
        elif delName < current.data:    # 삭제할 데이터가 트리 왼쪽에 있음
            if current.left == None:
                print(f'{delName} 트리에 없음')
                break
            else:
                parent = current
                current = current.left
        else:   # 삭제할 데이터가 트리 오른쪽에 있으면
            if current.right == None:
                print(f'{delName} 트리에 없음')
                break
            else:
                parent = current
                current = current.right
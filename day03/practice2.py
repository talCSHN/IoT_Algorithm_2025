import webbrowser
import time

# 스택 동작확인 구현

# 반복문에 사용되지 않는 변수(i)는 _로 변경 가능
SIZE = int(input('스택크기를 결정하세요 --> '))
stack = [None for _ in range(SIZE)]
top = -1

# 함수 선언
def isStackFull():  # 스택이 꽉 찼는지 확인하는 함수
    global SIZE, stack, top
    if top == (SIZE - 1):   # Full. ##참고 : 실무에서 쓰는 스택은 거의 무제한
        return True
    else:
        return False
    
def isStackEmpty():
    global SIZE, stack, top
    if top == -1:   # Empty
        return True
    else:
        return False
    
def push(data): # 스택에 데이터 추가
    global SIZE, stack, top
    if isStackFull():   # isStackFull() == True와 동일
        print('Stack is full')
        # return 생략
    else:
        top += 1
        stack[top] = data

def pop():  # 스택에서 데이터 추출
    global SIZE, stack, top
    if isStackEmpty():
        print('Stack is empty')
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return data
    
def peek(): # 스택의 top위치의 데이터 확인(살짝보기)
    global SIZE, stack, top
    if isStackEmpty():
        print('Stack is empty')
        return None
    else:
        return stack[top]
    
# 메인 모듈
if __name__ == '__main__':
    urls = ['naver.com', 'daum.net', 'nate.com']

print('스택종료')

webbrowser.open("http://www.hanbit.co.kr")


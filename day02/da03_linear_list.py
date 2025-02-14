# 선형리스트 일반 구현
# 실제 파이썬이 이렇게 동작하는게 아님
# 배열(선형리스트)가 어떻게 동작하는지 로직 파악

# 전역변수 선언
kakaoTalk = []  # 빈 배열
select = -1 # -1:통과, 1:추가, 2:삽입, 3:삭제, 4:종료

# 함수 선언
# 데이터 추가
def addData(friend):
    kakaoTalk.append(None)
    lenKakaoTalk = len(kakaoTalk)
    # print(len(kakaoTalk))
    kakaoTalk[lenKakaoTalk - 1] = friend

# 중간 데이터 삽입
def insertData(pos, friend):
    # 잘못된 인덱스를 넣었을 때 예외처리 필요
    if pos  < 0 or pos > len(kakaoTalk):
        print('실행할 범위를 벗어났습니다.')
        return
    
    kakaoTalk.append(None)
    lenKakaoTalk = len(kakaoTalk)

    for i in range(lenKakaoTalk - 1, pos, -1):    # 추가할 위치까지 데이터를 뒤로 이동
        kakaoTalk[i] = kakaoTalk[i - 1]
        kakaoTalk[i - 1] = None

    kakaoTalk[pos] = friend

# 데이터 삭제
def delData(pos):
    if pos < 0 or pos > len(kakaoTalk):
        print('삭제 범위를 벗어났습니다.')
        return
    lenKakaoTalk = len(kakaoTalk)
    kakaoTalk[pos] = None # 지정된 위치 값을 삭제

    for i in range(pos+1, lenKakaoTalk):
        kakaoTalk[i - 1] = kakaoTalk[i]
        kakaoTalk[i] = None

    del(kakaoTalk[lenKakaoTalk - 1])    # 배열 맨 마지막 삭제


if __name__ == '__main__':

    while True:
        select = int(input('선택(1:추가, 2:삽입, 3:삭제, 4:종료) > '))

        if select == 1:
            data = input('추가 데이터--> ')
            addData(data)
            print(kakaoTalk)
        elif select == 2:
            pos, data = input('삽입위치, 데이터 입력 > ').split()
            pos = int(pos)
            insertData(pos, data)
            print(kakaoTalk)
        elif select == 3:
            pos = int(input('삭제할 위치 > '))
            delData(pos)
            print(kakaoTalk)
        elif select == 4:
            break
        else:
            print('1 ~ 4 중 입력할 것')
            continue

from check_time import check_time
"""
어떠한 수 N이 1이 될때 까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 합니다.
단. 두번째 연산은 N이 K로 나누어 떨어질 때만 선택 할 수 있습니다.
1. N에서 1을 뺍니다.
2. N을 K로 나눕니다.
< example >
N = 17, K = 4
방법 1 실행 -> 1 N = 16, 
방법 2 2번 실행 -> N = 1
실행횟수 3
"""

@check_time
def main(N, K):
    temp_num = N
    cnt = 0
    while True:
        if temp_num < K:
            cnt = cnt + temp_num - 1
            break
        if temp_num == 1:
            break
        cnt = cnt + (temp_num % K) + 1
        temp_num = temp_num//K
    return cnt

@check_time
def greedy(N, K):
    temp_num = N
    cnt = 0 
    while True:
        if (temp_num % K) == 0:
            temp_num /= K
        else : 
            temp_num -= 1

        cnt += 1
        if temp_num == 1:
            break
        
    return cnt

@check_time
def answer_book(N, K):
    temp_num = N
    cnt = 0 
    while True:
        target = (temp_num // K) * K
        cnt += (temp_num - target)
        temp_num = target

        if temp_num < K:
            break
        cnt += 1
        temp_num //= K

    cnt += (temp_num - 1)
    return cnt

N, K = map(int, input("input number : ").split(' '))

print('result : ',main(N,K))
print('result : ',greedy(N,K))
print('result : ',answer_book(N,K))



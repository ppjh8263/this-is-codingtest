"""
정수 N이 입력되면 00시 00분 00초 부터 N시 59분 59초 까지의 모든 시각 중 
3이 하나라도 포함되는 모든 경우의 수를 구한느 프로그램을 작성하시오
"""


# 3, 13, 23 ->  3600
# 나머지 1575

# print(1575*5 + 3600)

# 3:00:00 -> 3600

# x:30:xx ~ x:39:59 -> 60 * 10
# x:x3:xx ~ -> 5개(30분 제외) 3분,13분 23분, 43분, 53분 -> 60 * 5
# x:xx:3x -> 10 * (60-10-5)

# 30분
# 각 x3분



def check_all_three(H):
    cnt = 0
    for H in range(H+1):
        for M in range(60):
            for S in range(60):
                if '3' in str(H)+str(M)+str(S):
                    cnt+=1


def check_three(H):
    if H < 3:
        return (H+1)*1575
    elif H < 13:
        return H*1575 + 3600
    elif H < 23:
        return (H-1)*1575 + 2 * 3600
    else :
        return (H-2)*1575 + 3 * 3600

H = int(input())

check_all_three(H)
check_three(H)
import os,sys
sys.path.append(
    os.path.dirname(
        os.path.abspath(os.path.dirname(__file__))))
        
from check_time import check_time
from itertools import combinations
""""
N개의 동전을 가지고 있다.
N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램
ex N=5. 화폐 단위 3,2,1,1,9원 동전
만들 수 없는 양의 정수 금액 최솟값 8
N = 3,3,5,7 양의 최솟값 1
첫째줄 동전의 개수
둘째줄 동전의 화폐 단위

5
3 2 1 1 9
"""


@check_time
def main(N,M,numbers):
    result = 0 
    for i,j in combinations(numbers,2):
        if i!=j:
            result+=1
    return result


if __name__ == '__main__':
    N, M = map(int,input().split())
    numbers = list(map(int,input().split()))
    print(main(N,M,numbers))
    # print(answer_book(N,numbers[:]))
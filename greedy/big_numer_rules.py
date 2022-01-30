import os,sys
sys.path.append(
    os.path.dirname(
        os.path.abspath(os.path.dirname(__file__))))
        
from check_time import check_time

"""
N크기 숫자의 리스트와 M과 K이 주어진다
배열에서 주어진 수들을 M번 더하여 가장 큰 수를 만들어야 하는데
특정 인덱스의 수를 K번 초과하여 연속으로 더할 수 없다.
첫 줄에 N, M, K가 주어지고
두번 째 줄에 자연수가 공백으로 구분되어 주어진다.
M >= K
"""
@ check_time
def main(numbers : list, M : int, K : int):
    sorted_numbers = sorted(numbers)
    first_value = sorted_numbers[-1]
    second_value = sorted_numbers[-2]
    
    return (first_value * K  + second_value) * M // (K + 1) + first_value * (M % (K + 1)) 


if __name__ == '__main__':
    N,M,K = map(int,input().split())
    numbers = list(map(int, input().split()))

    print(main(numbers,M,K))


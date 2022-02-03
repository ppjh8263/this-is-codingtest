"""
- 동빈이는 두개의 배열 A와 B를 가지고 있습니다.
두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수 입니다.
- 동빈이는 최대 K번의 바꿔치기 연산을 수행 할 수 있는데,
바꿔치기 연산이란 배열 A에 있는 원소하나와 배열 B에 있는 원소하나를 고라서
두 원소를 서로 바꾸는 것을 말합니다.
- 동빈이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이며,
여러분은 동빈이를 도와야 합니다.
- N, K 그리고 배열 A와 B의 정보가 주어졋을때, 최대 K번의 바꿔치기 연산을
수행하여 만들수 있는 배열 A의 모든 원소의 합의 최대값을 출력하는 프로그램을 작성하세요

"""
"""
5 3
1 2 5 4 3
5 5 6 6 5

26
"""


def main(A,B):
    A = sorted(A)
    B = sorted(B,reverse=True)

    for i in range(K):
        if A[i] < B[i]:
            A[i],B[i] = B[i],A[i]
        else :
            break

    return sum(A)

if __name__ == """__main__""":
    N,K = map(int,input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    print(main(A,B))
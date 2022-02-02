import os,sys
sys.path.append(
    os.path.dirname(
        os.path.abspath(os.path.dirname(__file__))))
        
from check_time import check_time

"""
N x M 크기의 얼음 틀이 있습니다. 
구멍이 뚫려 있는 부분은 0, 1로 표시됩니다.
구멍이 뚫려 있는 부분끼리 상,하,좌,우로 
붙어 있는 경우 서로 연결되어 있는 것으로 간주합니다.
이때, 얼음 틀의 모양이 주어졌을 때,
생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요

세로길이 N, 가로길이 M 첫줄
"""
"""
4 5
00110
00011
11111
00000
"""

def check_four_way(y,x):
    global ice_map
    if y > 0 and ice_map[y-1][x] == 0:
        ice_map[y-1][x]=2
        check_four_way((y-1),x)
    if y != (N-1) and ice_map[y+1][x] == 0:
        ice_map[y+1][x]=2
        check_four_way((y+1),x)
    if x > 0 and ice_map[y][x-1] == 0 :
        ice_map[y][x-1]=2
        check_four_way(y,x-1)
    if x != (M-1) and ice_map[y][x+1] == 0 :
        ice_map[y][x+1]=2
        check_four_way(y,x+1)

@check_time
def main():
    cnt = 0
    for n in range(N):
        for m in range(M):
            if ice_map[n][m] == 0:
                ice_map[n][m]=2
                check_four_way(n,m)
                cnt += 1

    return cnt

def dfs(y,x):
    if y <= -1 or y >= N or x <= -1 or x >=M:
        return False
    if ice_map[y][x] == 0:
        ice_map[y][x] = 1
        dfs(y-1,x)
        dfs(y+1,x)
        dfs(y,x-1)
        dfs(y,x+1)
        return True
    return False

@check_time
def answer_book():
    cnt = 0
    for n in range(N):
        for m in range(M):
            if dfs(n,m):
                cnt += 1

    return cnt

if __name__ == '__main__':
    N, M = map(int, input().split())
    ice_map =[]
    for i in range(N):
        ice_map.append(list(map(int,input())))

    print(main())
    # print(answer_book())


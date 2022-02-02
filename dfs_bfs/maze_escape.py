import os,sys
sys.path.append(
    os.path.dirname(
        os.path.abspath(os.path.dirname(__file__))))
        
from check_time import check_time
from collections import deque

"""
N * M 크기의 직사각형 형태의 미로에 갇힘
여러마리의괴물이 있어 이를 피해야함
시작 위치는 1,1 미로의 출구는 N,M의 위치 한번에 한칸 이동 가능
괴물이 잇는 부분은 0 없는 부분은 1
미로는 반드시 탈출 할 수 있는 형태로 제시
동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오
칸을 셀때는 시작 칸과 마지막 칸을 모두 포함해서 계산합니다.
"""
"""
5 6
101010
111111
000001
111111
111111
"""

def check_four_way(y,x):
    global maze
    count = maze[y][x]+1
    for i in range(4):
        temp_y = y+dy[i]
        temp_x = x+dx[i]
        if temp_y >= 0 and temp_y < N and temp_x >=0 and temp_x < M:
            if maze[temp_y][temp_x] == 1:
                maze[temp_y][temp_x]=count
                if temp_y == N-1 and temp_x == M-1:
                    return maze[N-1][M-1]
                check_four_way(temp_y,temp_x)
    return maze[N-1][M-1]

@check_time
def main(y,x):
    return check_four_way(y,x)

@check_time
def bfs(y,x):
    global maze
    queue = deque()
    queue.append((y,x))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= N or nx < 0 or ny >=M:
                continue
            if maze[ny][nx]==0:
                continue
            if maze[ny][nx] ==1:
                maze[ny][nx] = maze[y][x] + 1
                queue.append((ny,nx))
    return maze[N-1][M-1]

if __name__ == '__main__':
    y,x = 0, 0

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    N,M = map(int,input().split())

    maze = [list(map(int,input())) for i in range(N)]

    # result = main()
    result1 = main(y,x)
    # result2 = bfs(y,x)

    print("===============result===============")
    print(f'result1 : {result1}')
    # print(f'result2 : {result2}')
    # for m in maze:
    #     print(m)     
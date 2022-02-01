"""
N * M 크기의 직사각형
맵의 각 칸은 (A, B) A는 북쪽으로 부터 떨어진 칸의 개수,  B서쪽으로 부터 떨어진 개수
캐릭터는 상하좌우로 움직일 수 있고 바다로 되어 있는 공간에는 갈 수 없다.
1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈곳을 정한다
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽방향으로 회전한 다음 왼쪽으로 한칸을 전진한다.
왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
3. 만약 네방향 모두 이미 가본 칸ㅇ이거나 바다로 되어 있는 칸인 경우, 바라보는 방향을 유지한 채로 한칸 뒤로 가고 1단계로 돌아간다.
단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

<입력>
첫째 줄에 맵의 세로 크기 N M 공백 구분(N >= 3, M <= 50)
둘째줄 게임 캐릭터 위치 좌표 A,B 바라보는 방향 d 서로 공백으로 주어짐
0 : 북, 1 : 동, 2 : 남, 3 : 서
셋째 줄 부터 바다인지 육지인지 입력
0 -> 육지
1 -> 바다
맵 외각은 항상 바다
캐릭터는 육지에서 시작
"""
"""
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

-> 3
"""

N, M = map(int,input().split())
A,B,d = map(int,input().split())
game_map = []
for n in range(N):
    game_map.append(list(map(int,input().split())))

dA=[-1, 0, 1, 0]
dB=[0, 1, 0, -1]

go = 2
game_map[A][B]=go
go += 1
result = 1

def view_left(A,B,d):
    view = {
        0:[game_map[A][B-1],A,B-1],
        1:[game_map[A-1][B],A-1,B],
        2:[game_map[A][B+1],A,B+1],
        3:[game_map[A+1][B],A+1,B],
    }
    return view[d][0],view[d][1],view[d][2]

def view_back(A,B,d):
    view = {
        0:[game_map[A-1][B],A-1,B],
        1:[game_map[A][B-1],A,B-1],
        2:[game_map[A+1][B],A+1,B],
        3:[game_map[A][B+1],A,B+1],
    }
    return view[d][0],view[d][1],view[d][2]

cnt = 0
def next_d(d):
    d -= 1
    if d == -1:
        d = 3
    return d
while True:
    # print(f"A:{A},B:{B},d:{d}")
    next_tile,next_A,next_B = view_left(A,B,d)
    # print(f"next... tile:{next_tile}, next_A:{next_A},next_B:{next_B}")
    # print(".....")
    # print()
    if next_tile == 0:
        d = next_d(d)
        A = next_A
        B = next_B
        game_map[A][B] = go
        go += 1
        result += 1
        cnt = 0
    else:
        d = next_d(d)
        cnt += 1
        if cnt == 4:
            cnt = 0
            next_tile,next_A,next_B = view_back(A,B,d)
            if next_tile == 1:
                break
            else :
                A = next_A
                B = next_B 


# game_map[A][B] = 20
print("========result=========")
# print(game_map)
for m in game_map:
    print(m)
print(result)

"""
10 10
1 1 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
"""


# [1,  1,  1,  1,  1,  1,  1,  1,  1,  1]
# [1,  2,  3,  4,  5,  6,  7,  8,  9,  1]
# [1, 28, 29, 30, 31, 32, 33, 34, 10,  1]
# [1, 27, 45, 46, 47, 48, 49, 35, 11,  1]
# [1, 26, 44,  0,  0,  0, 50, 36, 12,  1]
# [1, 25, 43, 42, 41, 40, 39, 37, 13,  1]
# [1, 24,  0,  0,  0,  0,  0, 38, 14,  1]
# [1, 23, 22, 21, 20, 19, 18, 17, 15,  1]
# [1,  0,  0,  0,  0,  0,  0,  0, 16,  1]
# [1,  1,  1,  1,  1,  1,  1,  1,  1,  1]
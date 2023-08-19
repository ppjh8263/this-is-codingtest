"""
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 
어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.
체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 
구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 
변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 
따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 
하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 
지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 
당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

출력
첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.
"""


"""
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
"""
import sys
input = lambda : sys.stdin.readline().rstrip()
maps = []
N, M = map(int, input().split())

for _ in range(N):
    maps.append(input())

def change_color(color):
    if color == "B":
        return "W"
    elif color == "W":
        return "B"

def cnt_color_chnage(start_color) -> list:
    tmp_color = change_color(start_color)
    cnt_maps = [[0 for _ in range(M)] for _ in range(N)]
    for n in range(N):
        for m in range(M):
            if tmp_color == maps[n][m]:
                cnt_maps[n][m] = 1
                tmp_color = change_color(tmp_color)
            else:
                tmp_color = maps[n][m]
        if cnt_maps[n][0] == 1:
            tmp_color = change_color(maps[n][0])
        else:
            tmp_color = maps[n][0]
    return cnt_maps

cnt_color_w = cnt_color_chnage('W')
cnt_color_b = cnt_color_chnage('B')
result = 999999999
for n in range(N-8+1):
    for m in range(M-8+1):
        tmp_w = 0
        tmp_b = 0
        for w in cnt_color_w[n:n+8]:
            tmp_w += sum(w[m:m+8])
        for b in cnt_color_b[n:n+8]:
            tmp_b += sum(b[m:m+8])
        
        result = min(result, tmp_w, tmp_b)

print(result)



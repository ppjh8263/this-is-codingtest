"""
여행가 A는 N * N 크기의 정사각형 공간 위에 서 있습니다.
이 공간은 1 * 1 크기의 정사각형으로 나누어져 있습니다.
가장 왼쪽 위 좌표는 (1,1)이며, 가장 오른 쪽 아래 좌표는 (N,N)입니다.
여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며,
시작좌표는 항상 (1,1)입니다.
우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있습니다
계획서에는 하나의 줄에 띄어쓰기를 기준 L, R, U, D문자가 반복적으로 적혀 있습니다.
이때 공간을 벗어나는 움직임은 무시됩니다.
"""


def move_location(loc,moving,N):
    y = check_outting(loc[0]+moving[0],N)
    x = check_outting(loc[1]+moving[1],N)
    return (y,x)


def check_outting(point,size):
    if point >= size+1:
        return size
    elif point <= 0:
        return 1
    else:
        return point

def main(N, move_plan):
    location = (1, 1)

    dict_move = {'L' : (0, -1), 'R' : (0, 1), 'U' : (-1,0), 'D' : (1, 0),}

    for plan in move_plan:
        location = move_location(location, dict_move[plan], N)

    return location
    

if __name__ == '__main__':
    N = int(input())
    move_plan = input().split()
    y, x = main(N,move_plan)
    print(f'{y} {x}')


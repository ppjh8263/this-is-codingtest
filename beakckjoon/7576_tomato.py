# M, N = map(int, input().split(' '))
M, N = 6, 4

import sys
input = sys.stdin.readline
M, N = map(int, input().split(' '))
arr = []
for n in range(N):
    arr.append(list(map(int,input().split(' '))))

print(arr)


def change_toamto(arr, y, x):
    if check_is_toamto(arr, y, x):

    else:
        return arr
    
        arr[dx - 1][dy] = 1
        arr[dx + 1][dy] = 1
        arr[dx][dy - 1] = 1
        arr[dx][dy + 1] = 1
    else:
        raise ValueError('arr[dx][dy] is not 0, -1, 1')

def check_is_toamto(arr,x,y):
    if arr[y][x] == 0:
        return True
    elif arr[y][x] == -1:
        return False
    elif arr[y][x] == 1:
        return True
    else:
        raise ValueError('arr[x][y] is not 0, -1, 1')
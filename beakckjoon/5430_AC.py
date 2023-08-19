"""R(뒤집기)과 D(버리기)가 있다.
함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고, 
D는 첫 번째 수를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.
"""

import sys
input = sys.stdin.readline

T = int(input())
inputs = []

for _ in range(T):
    command = input().rstrip()
    n = int(input().rstrip())
    target_list = eval(input().rstrip())
    inputs.append((command,n,target_list))


for command, n, lst in inputs:
    reverse = False
    is_break = False
    for cmd in command:
        if cmd == 'R':
            reverse = not reverse
        elif cmd == 'D':
            if len(lst) == 0:
                is_break = True
                break
            if reverse:
                lst.pop()
            else:
                lst.pop(0)
    
    if is_break:
        print("error")
    elif reverse:
        lst.reverse()
        print(f"[{','.join(map(str,lst))}]")
    else:
        print(f"[{','.join(map(str,lst))}]")
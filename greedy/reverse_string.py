import os,sys
sys.path.append(
    os.path.dirname(
        os.path.abspath(os.path.dirname(__file__))))
        
from check_time import check_time
"""
다솜이는 0과 1로만 이루어진 문자열 S를 가지고 있습니다.
다솜이는 이 문자열 S에 있는 모든숫자를 전부 같게 만들려고 합니다.
다솜이가 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것입니다.
뒤집는것은 1을 0으로, 0을 1로 바꾸는 것을 의미합니다.
ex)
S = 0001100
1. 전체를 뒤집으면 11을 뒤집으면 0000000 1번만에 바로 모든 같은 숫자
"""


@check_time
def main(numbers):
    count = [0,0]
    temp_n = -1
    group = 0
    groups ={0:1,1:0}
    for n in numbers:
        if temp_n != n:
            temp_n = n
            count[group]+=1
            group = groups[group]

    return min(count)



if __name__ == '__main__':
    numbers = input()
    print(main(numbers))

"""
행복 왕국의 왕실 정원은 체스판과 같은 8 * 8 좌표 평면 입니다.
왕실 정원의 틍정한 한칸에 나이트가 서 있습니다
나이트는 매우 충성스러운 신하로서 매일 무술을 연마합니다
나이트는 말을 타고 있기 때문에 이동할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없습니다.
나이트는 특정 위치에서 다음과 같은 2가지 경으ㅜ로 이동 할 수 있습니다.
1. 수평으로 두칸 이동한 뒤에 수직으로 한칸 이동하기
2. 수직으로 두칸 이동한 뒤에 수평으로 한칸 이동하기

나이트의 위치가 주어 졌을때 나이트가 이동 할 수 있는 모든 경우의 수를 출력하는 프로그램을 작성하시오
"""

# 0,0

"""
방법 1 -> (1,2),(-1,2),(1,-2),(-1,-2)
방법 2 -> (2,1),(-2,1),(2,-1),(-2,-1)
"""
# loc = y,x


def calc_loc(loc,move):
    return (loc[0]+move[0],loc[1]+move[1])

def check_outting(point,size=8):
    return point > 0 and point <= size

def check_location(loc,size=8):
    return check_outting(loc[0]) and check_outting(loc[1])

def main(input_loc):
    loc_x = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
    loc = (int(input_loc[1]),loc_x[input_loc[0]])
    move_pattern = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1)]
    count = 0
    for p in move_pattern:
        if check_location(calc_loc(loc,p)):
            count += 1

    return count
    
if __name__=='__main__':
    input_loc = input()
    print(main(input_loc))

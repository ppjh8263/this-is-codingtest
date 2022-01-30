from check_time import check_time

"""
각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을 때, 
왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하여 숫자 사이에 'x' 혹은 '+' 연산을 넣어
결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오
단 +보다 x를 먼저 계산하는 일반적인 방식과 달리, 모든 연산은 왼쪽에서 부터 순서대로 이루어 집니다.
"""
@check_time
def main(list_number):
    result = list_number[0]
    for idx in range(1, len(list_number)):
        result = max([result * list_number[idx], result + list_number[idx]])
    return result

@check_time
def answer_book(list_number):
    result = list_number[0]
    for idx in range(1, len(list_number)):
        if (result <= 1) or (list_number[idx] <= 1):
            result += list_number[idx]
        else :
            result *= list_number[idx]
    return result

if __name__ == '__main__':
    input_numbers = list(map(int, input("input numbers : ")))
    print(main(input_numbers))
    print(answer_book(input_numbers))
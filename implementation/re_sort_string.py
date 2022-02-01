"""
알파벳 대문자와 숫자로만 구성된 문자열이 입력으로 주어집니다.
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에 모든 숫자를 더한값을 이어서 출력
"""
import re

input_str = input()

compile_number = re.compile('\d')
compile_str = re.compile('\D')

numbers = sum(map(int,compile_number.findall(input_str)))
strings = ''.join(sorted(compile_str.findall(input_str)))

print(f'{strings}{numbers}')
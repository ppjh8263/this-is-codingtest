import sys
input = lambda : sys.stdin.readline().rstrip()

inputs = []
while True:
    _input = input()
    if _input == '0':
        break
    else:
        inputs.append(_input)

# result = []
for _input in inputs:
    tmp_result = 'yes'
    l = len(_input)
    for i in range(l):
        if _input[i] != _input[l - i - 1]:
            tmp_result = 'no'
            break
        if i > l / 2:
            break
    print(tmp_result)
    
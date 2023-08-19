import sys

input = sys.stdin.readline
N = int(input().rstrip())
ox_inputs = []
for _ in range(N):
    ox_inputs.append(input().rstrip())

for ox_input in ox_inputs:
    last_score = 0
    score = 0
    for ox in ox_input:
        if ox == "O":
            tmp_score = 1
        else:
            tmp_score = 0
            last_score = 0
        
        last_score += tmp_score
        score += last_score
    print(score)
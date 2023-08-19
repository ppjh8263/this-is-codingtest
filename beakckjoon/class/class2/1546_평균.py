import sys
input = lambda : sys.stdin.readline().rstrip()
N = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)
def f(x):
    return x/max_score*100

print(sum(map(f, scores))/N)
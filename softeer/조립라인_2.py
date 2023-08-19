import sys

input = sys.stdin.readline
N = int(input().rstrip())

b_offset = N + 1

times_dp = {
    "A" : [[] for _ in range(N + 1)],
    "B" : [[] for _ in range(N + 1)]
    }
times_dp["A"][0] = 0
times_dp["B"][0] = 0
times = []
for i in range(N - 1):
    times.append(map(int, input().split()))
a,b = map(int, input().split())
times.append((a,b,0,0))

pre_atob, pre_btoa = 0, 0
for i, (a, b, atob, btoa) in enumerate(times):
    times_dp["A"][i + 1] = min(
        times_dp["A"][i] + a,
        times_dp["B"][i] + pre_btoa + a,
        )
    times_dp["B"][i + 1] = min(
        times_dp["B"][i] + b,
        times_dp["A"][i] + pre_atob + b,
    )   
    pre_atob, pre_btoa = atob, btoa
print(min(times_dp["A"][-1],times_dp["B"][-1]))
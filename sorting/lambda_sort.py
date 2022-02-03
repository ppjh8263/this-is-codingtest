N = int(input())

scores=[]
for n in range(N):
    name,score = input().split()
    scores.append([name, int(score)])

scores = sorted(scores,key=lambda arr:arr[1])
print(scores)

result  = [score[0] for score in scores]
print(result)
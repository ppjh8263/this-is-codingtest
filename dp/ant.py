import time
def main(N, K):
    dict_memo = {}
    for i, k in enumerate(K):
        if i == 0 or i == 1:
            dict_memo[i] = k
            continue
        dict_memo[i] = max(dict_memo[i-1], dict_memo[i-2]+k)
    
    return dict_memo[i]
    
def main2(N, K):
    list_memo = [0 for _ in range(N)]
    for i, k in enumerate(K):
        if i == 0 or i == 1:
            list_memo[i] = k
            continue
        list_memo[i] = max(list_memo[i-1], list_memo[i-2]+k)
    
    return list_memo[-1]

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    N = int(input())
    K = map(int,input().split())
    t1 = time.time()
    print(main(N, K))
    # print(main2(N, K))
    print(time.time()-t1)
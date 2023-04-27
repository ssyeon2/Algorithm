import sys
input = sys.stdin.readline
N, q = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

prefix_sum = [0]
temp = 0
for i in arr:
    temp +=i
    prefix_sum.append(temp)
    
for j in range(q):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])
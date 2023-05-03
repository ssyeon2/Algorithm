import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

a.sort()
count = 0

for i in range(N):
    find = a[i]
    start = 0
    end = N -1
    while start < end:
        if a[start] + a[end] == find:
            if (start != i) & (end != i):
                count += 1
                break
            elif end == i :
                end -= 1
            elif start == i:
                start += 1
        elif a[start] + a[end] < find :
            start += 1
        else :
            end -= 1
print(count)
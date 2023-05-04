import sys
input = sys.stdin.readline
N = int(input())
first = []
maxi = 0
for i in range(N):
    first.append((int(input()), i))

second = sorted(first)

for i in range(N):
    substract = second[i][1] - i
    if substract > maxi:
        maxi = substract
print(maxi + 1)
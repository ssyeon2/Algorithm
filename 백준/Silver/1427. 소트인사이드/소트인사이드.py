import sys
input = sys.stdin.readline

A = list(input())

for i in range(len(A)):
    for j in range(i+1, len(A)):
        maxi = A[i]
        if A[j] > maxi:
            A[i], A[j] = A[j], A[i]
print(''.join(A))
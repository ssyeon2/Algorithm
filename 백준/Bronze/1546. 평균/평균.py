N = int(input())
score = list(map(int, input().split(' ')))

maxi = max(score)

mean = 0
for i in score :
    mean += (i / maxi) * 100
print(mean/N)
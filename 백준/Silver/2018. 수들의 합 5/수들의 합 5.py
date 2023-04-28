import sys
input = sys.stdin.readline

N = int(input())

count = 1
start_point = 1
end_point = 1
sum = 1

while end_point != N :
    if sum == N :
        count+=1
        end_point += 1
        sum+= end_point
    elif sum > N:
        sum -= start_point
        start_point +=1
    else:
        end_point +=1
        sum += end_point

print(count)
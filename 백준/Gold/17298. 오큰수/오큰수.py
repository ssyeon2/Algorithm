n = int(input())
answer = ['-1']*n
nums = list(map(int, input().split()))
myStack = []

for i in range(n):
    while myStack and nums[myStack[-1]] < nums[i]:
        answer[myStack.pop()] = str(nums[i])
    myStack.append(i)

print(' '.join(answer))
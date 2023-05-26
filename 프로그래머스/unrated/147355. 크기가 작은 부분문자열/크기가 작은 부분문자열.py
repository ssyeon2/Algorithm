def solution(t, p):
    result = []
    for i in range(len(t) - len(p) + 1):
        answer = ''
        for j in range(len(p)):
            answer += t[i+j]
        result.append(answer)
    count = 0
    for k in range(len(result)):
        if int(result[k]) <= int(p):
            count += 1
    return count
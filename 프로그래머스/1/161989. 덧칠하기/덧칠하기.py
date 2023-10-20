def solution(n, m, section):
    count = 1
    paint = section[0] # 덧칠 시작 지점
    for i in range(1, len(section)):
        if section[i] - paint >= m  :
            count+=1
            paint = section[i]
    answer = count
    return answer
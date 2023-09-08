# 딕셔너리 생성
import math
def solution(fees, records):
    min = 0
    number = {}
    for i in range(len(records)):
        number[records[i][6:10]] = 0

    # 시간 계산하기
    for i in range(len(records)):
        count = 0
        if records[i][-1] == 'N':
            for j in range(i+1, len(records)):
                if records[i][6:10] == records[j][6:10]:
                    hour = abs(int(records[j][0:2]) - int(records[i][0:2]))
                    if int(records[j][3:5]) <= int(records[i][3:5]):
                        hour = hour- 1
                        min = int(records[j][3:5])+60 - int(records[i][3:5])
                    else:
                        min = abs((int(records[j][3:5]) - int(records[i][3:5])))
                    hour = hour * 60

                    number[records[i][6:10]] += (hour + min)
                    count += 1
                    break
            if count == 0 :
                hour = 23 - int(records[i][0:2])
                min = 59 - int(records[i][3:5])
                hour = hour * 60
                number[records[i][6:10]] += (hour + min)

    # 정렬
    number = dict(sorted(number.items(), key = lambda item : item[0]))

    # 가격 계산
    answer = []
    for k in number:
        # 가격 계산
        if number[k] <= fees[0] :
            answer.append(fees[1])
        else:
            answer.append(fees[1] + (math.ceil((number[k] - fees[0]) / fees[2]) * fees[3]))
    return answer
def solution(name, yearning, photo):
    answer = [0 for i in range(len(photo))]
    missdict = {}
    for i in range(len(name)):
        missdict[name[i]] = yearning[i]
    
    for i in range(len(photo)):
        for each in photo[i]:
            if each in missdict:
                answer[i] += missdict[each]    
    return answer
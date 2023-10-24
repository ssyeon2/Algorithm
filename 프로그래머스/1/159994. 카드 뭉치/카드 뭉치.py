def solution(cards1, cards2, goal):
    count=0
    for word in cards2:
        for i in range(len(goal)):
            if word == goal[i]:
                cards1.insert(i, word)
                count+=1
    card = ''.join(cards1)
    goal = ''.join(goal)
    if goal in card :
        answer = 'Yes'
    else :
        answer = 'No'
    return answer
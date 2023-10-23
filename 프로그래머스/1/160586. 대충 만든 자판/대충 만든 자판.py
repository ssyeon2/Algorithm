def solution(keymap, targets):
    answer = [0 for i in range(len(targets))]
    for j in range(len(targets)):
        roof = 0
        count = 0
        for target in range(len(targets[j])) :
            result = []
            for key in range(len(keymap)):
                for i in range(len(keymap[key])) :
                    word = keymap[key][i]
                    if targets[j][target] == word :
                        result.append(i+1)
            if len(result) == 0:
                count = -1
                break
            else :
                count+= min(result)
        answer[j] =count
    return answer
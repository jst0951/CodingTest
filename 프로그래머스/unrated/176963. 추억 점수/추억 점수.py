def solution(name, yearning, photo):
    yearning_dict = {}
    for i in range(len(yearning)):
        yearning_dict[name[i]] = yearning[i]

    result = []
    for group in photo:
        score = 0
        for person in group:
            if person in yearning_dict:
                score += yearning_dict[person]
        result.append(score)
    
    return result
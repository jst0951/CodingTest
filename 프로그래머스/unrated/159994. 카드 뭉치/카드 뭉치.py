def solution(cards1, cards2, goal):
    while len(goal) > 0:
        if len(cards1) > 0:
            if goal[0] == cards1[0]:
                goal.pop(0)
                cards1.pop(0)
                continue
        if len(cards2) > 0:
            if goal[0] == cards2[0]:
                goal.pop(0)
                cards2.pop(0)
                continue
        return "No"
    return "Yes"
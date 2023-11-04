def solution(n):
    hanoi(n, 1, 3, 2)
    return move_list

move_list = []
def hanoi(n, start, end, aux):
    global move_list
    if n == 1:
        move_list.append([start, end])
    else:
        # 보조 판으로 n-1개 이동
        hanoi(n-1, start, aux, end)
        move_list.append([start, end])
        # 목표 판으로 n-1개 이동
        hanoi(n-1, aux, end, start)
    
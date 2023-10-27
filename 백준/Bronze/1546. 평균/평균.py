N = int(input())

score_list = list(map(int, input().split()))

max_score = max(score_list)
score_list = [score/max_score*100 for score in score_list]

print(sum(score_list) / len(score_list))
from itertools import permutations
import math
def solution(numbers):
    number_list = list(numbers)
    permu_list = []
    for i in range(1, len(number_list)+1):
        permu = list(permutations(number_list, i))
        permu_list.extend(permu)

    comb_set = set()
    for permu in permu_list:
        number = int(''.join(permu))
        comb_set.add(number)
        
    comb_list = list(comb_set)
    comb_list.sort()
    
    count = 0
    for comb in comb_list:
        if is_prime_number(comb):
            count += 1

    return count

def is_prime_number(num):
    if num <= 1:
        return False
    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            return False
    return True
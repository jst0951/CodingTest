from math import gcd

def get_measure_list(n):
    measure_list = []
    for x in range(2, n+1):
        if n % x == 0:
            measure_list.append(x)
    return measure_list

def solution(arrayA, arrayB):
    gcd_A = arrayA[0]
    gcd_B = arrayB[0]
    for i in range(len(arrayA)):
        gcd_A = gcd(gcd_A, arrayA[i])
    for i in range(len(arrayB)):
        gcd_B = gcd(gcd_B, arrayB[i])
    
    measure_A_list = get_measure_list(gcd_A)
    measure_B_list = get_measure_list(gcd_B)
    
    result_list = []
    for measure_A in measure_A_list:
        isValid = True
        for num in arrayB:
            if num % measure_A == 0:
                isValid = False
                break
        if isValid == True:
            result_list.append(measure_A)
    
    for measure_B in measure_B_list:
        isValid = True
        for num in arrayA:
            if num % measure_B == 0:
                isValid = False
                break
        if isValid == True:
            result_list.append(measure_B)
    
    if len(result_list) == 0:
        return 0
    else:
        return max(result_list)
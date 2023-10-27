M, N = list(map(int, input().split()))
from math import sqrt
def isPrime(number):
    if number == 1:
        return False
    for div in range(2, int(sqrt(number))+1):
        if number % div == 0:
            return False
    return True

for num in range(M, N+1):
    if isPrime(num) == True:
        print(num)


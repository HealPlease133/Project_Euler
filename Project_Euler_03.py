# 어떤 수를 소수의 곱으로만 나타내는 것을 소인수분해라 하고, 이 소수들을 그 수의 소인수라고 합니다.
# 예를 들면 13195의 소인수는 5, 7, 13, 29 입니다.

# 600851475143의 소인수 중에서 가장 큰 수를 구하세요.

def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(num):
    value = 2
    while not isPrime(num):
        if isPrime(value) and num % value == 0:
            num //= value
        value += 1
    return num
    
print(solution(600851475143))

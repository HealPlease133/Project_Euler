# 1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.

# 그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?

def isPrime(num):
    primes = []
    while num != 1:
        for i in range(2,num + 1):
            if num % i == 0:
                primes.append(i)
                num //= i
    return primes
        
def solution(num):
    
    
print(solution(20))

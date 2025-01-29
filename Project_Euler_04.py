# 앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부릅니다.

# 두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다.

# 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?

def findPalindrome(num):
    if str(num) == "".join(reversed(str(num))):
        return True
    return False

def solution():
    maxNum = 0
    
    for i in range(1,1000):
        for k in range(1,1000):
            if findPalindrome(i * k) and maxNum < i * k:
                maxNum = i * k
    return maxNum
    
print(solution())

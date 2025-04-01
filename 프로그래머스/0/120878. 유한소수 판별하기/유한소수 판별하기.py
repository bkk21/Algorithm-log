import math
def solution(a, b):
    answer = 2
    
    #최소공배수 구하기
    gcd_num = math.gcd(a, b)
    print(gcd_num)
    
    #기약 분수 만들기
    if gcd_num != 1 and a % gcd_num == 0:
        a = a // gcd_num
        b = b // gcd_num
    
    nums = []
    
    for i in range(2, b+1):
        while b % i == 0:
            if b % i == 0:
                if i not in nums: 
                    nums.append(i)
                b = b // i
        if b == 1:
            break
    
    print(nums)
    
    #2와 5삭제
    if 2 in nums:
        nums.remove(2)
    if 5 in nums:
        nums.remove(5)
    
    if nums == []:
        answer = 1
    
        
    return answer
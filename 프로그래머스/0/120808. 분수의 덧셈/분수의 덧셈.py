import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    new1 = numer1 * denom2 + numer2 * denom1
    new2 = denom1 * denom2
    
    gcd = math.gcd( new1, new2 )
    
    if gcd != 1:
        new1 = new1 // gcd
        new2 = new2 // gcd
    
    answer = [new1, new2]
    return answer
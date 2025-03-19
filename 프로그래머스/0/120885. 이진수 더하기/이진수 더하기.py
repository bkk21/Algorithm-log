def solution(bin1, bin2):
    answer = bin(int(bin1, 2) + int(bin2, 2)).split('b')[1]
    
    return answer
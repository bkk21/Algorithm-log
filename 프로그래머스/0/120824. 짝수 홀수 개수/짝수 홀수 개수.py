def solution(num_list):
    tmp = len([x for x in num_list if x % 2 == 0])
    answer = [ tmp, len(num_list) - tmp]
    return answer
#선택할 수 있는 종류 구하기

def solution(nums):
    
    #가져갈 수 있는 포켓몬 수(절반)
    num = len(nums) // 2
    
    #임시 리스트 생성
    tmp = list()
    
    for i in range(len(nums)):
        #처음 일 떄
        if i == 0:
            tmp.append(nums[i])
            result = 1
            
        #아직 가져갈 수 있는 종류가 남아있는지
        elif result < num:
            #중복인지 확인
            if nums[i] in tmp:
                continue
            else:
                tmp.append(nums[i])
                result += 1
    
    if num <= result:
        result = num

    return result
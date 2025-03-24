def solution(numbers):
    answer = ''
    number = {'ze' : '0', 'on':'1', 'tw':'2', 'th':'3', 'fo':'4', 'fi':'5', 'si':'6', 'se':'7',
              'ei':'8', 'ni':'9'}
    
    for i in range(len(numbers) - 1):
        text = numbers[i:i+2]
        #print(text)
        
        if text in number.keys():
            answer += number[text]
        
    return int(answer)
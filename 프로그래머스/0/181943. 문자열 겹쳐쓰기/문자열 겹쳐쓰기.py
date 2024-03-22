def solution(my_string, overwrite_string, s):
    new_string = ""
    
    for i in range(len(my_string)):
        if i >= s and i < (len(overwrite_string) + s):
            new_string += overwrite_string[i - s]
        else:
            new_string += my_string[i]
        
            
    return new_string
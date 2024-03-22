def solution(myString):
    result = ""
    for i in range(len(myString)):
        
        if myString[i] == "a" or myString[i] == "A":
            result += myString[i].upper()
            
        else:
            result += myString[i].lower()
    
    return result
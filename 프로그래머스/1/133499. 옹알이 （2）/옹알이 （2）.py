def solution(babbling):
    can_pronounce = ['aya','ye','woo','ma']
    cant_pronounce = ['ayaaya','yeye','woowoo','mama']
    answer = 0
    
    for word in babbling:
        for char in cant_pronounce : 
            if char in word:
                word = word.replace(char,'x')
        for char in can_pronounce : 
            if char in word:
                word = word.replace(char,' ')
        
        word = word.replace(' ','')
        if word == '':
            answer += 1
        
    return answer
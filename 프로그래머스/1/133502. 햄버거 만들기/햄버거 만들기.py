def solution(ingredient):
    answer = 0
    st = [] 
    for i in range(len(ingredient)):
        st.append(ingredient[i])
        if(len(st) >= 4 and ingredient[i] == 1): #1:빵, 2:야채, 3:고기 
            n = len(st)
            if st[-2] == 3 and st[-3] == 2 and st[-4] == 1:
                for i in range(4):
                    st.pop()
                answer+=1

    return answer
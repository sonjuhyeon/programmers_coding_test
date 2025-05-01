def solution(numbers):
    answer = []
    for n in numbers:
        bin_n = list(bin(n)[2:])
        if '0' in bin_n:
            if bin_n[-1] == '0':
                bin_n[-1] = '1'
                bin_n = ''.join(bin_n)
                answer.append(int(bin_n, 2))
            else:
                for i in range(len(bin_n) - 1, -1, -1):
                    if bin_n[i] == '0':
                        bin_n[i] = '1'
                        bin_n[i + 1] = '0'
                        break
                bin_n = ''.join(bin_n)
                answer.append(int(bin_n, 2))
        else:
            bin_n = ['1'] + bin_n
            bin_n[1] = '0'
            bin_n = ''.join(bin_n)
            answer.append(int(bin_n, 2))
    return answer
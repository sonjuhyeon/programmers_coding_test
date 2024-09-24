def solution(lines):
    answer = 0 
    lines.sort(key=lambda x: x[0])
    cs, ce = lines[0]

    for line in lines[1:]:
        s, e = line
        if ce <= s:
            cs, ce = s, e
            continue

        maxs, mine, maxe = max(cs, s), min(ce, e), max(ce, e)
        answer += abs(mine - maxs)
        cs, ce = mine, maxe

    return answer
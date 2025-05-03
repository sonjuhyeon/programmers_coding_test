from itertools import product

def solution(users, emoticons):
    discount_rates = [10, 20, 30, 40]
    result = []
    
    # 이모티콘 개별 할인율의 모든 조합 구하기
    discount_cases = list(product(discount_rates, repeat=len(emoticons)))

    for discount_case in discount_cases:
        members = 0
        income = 0

        for required_discount, budget in users:
            purchased = 0
            for i in range(len(emoticons)):
                # 사용자가 구매할 이모티콘
                # 각 조합별 모든 이모티콘을 순회하며 경우의 수 구하기
                if required_discount <= discount_case[i]:
                    # 한 사용자의 구매액은 자신의 기준 할인율 이상 할인하는 이모티콘의 할인가
                    purchased += emoticons[i] - emoticons[i] * discount_case[i] * 0.01
            if purchased >= budget:
                # 총 구매액이 사용자의 예산 이상이라면, 구매하지 않고 플러스 가입
                members += 1
            else:
                # 그렇지 않다면 이모티콘 구매하므로 총 판매금액에 합산    
                income += purchased
        # 할인율 조합별 총 가입자수와 판매액을 배열에 저장
        result.append((members, income))
    # 조합별 가장 가입자수 > 판매액 순으로 큰 경우를 찾아 리턴
    answer = sorted(result, reverse=True, key=lambda x: (x[0], x[1]))

    return answer[0]
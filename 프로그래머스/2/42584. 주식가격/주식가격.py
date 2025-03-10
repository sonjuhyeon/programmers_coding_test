from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:
        count = 0
        price = prices.popleft()

        for p in prices:
            if price <= p:
                count += 1
            else:
                count += 1
                break
        answer.append(count)
    return answer
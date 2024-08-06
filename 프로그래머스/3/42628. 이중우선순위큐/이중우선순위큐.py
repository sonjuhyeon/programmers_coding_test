def solution(operations):
    answer = []
    queue = []
    for s in operations:
        tasks = s.split(" ")
        if tasks[0] == "I":
            queue.append(int(tasks[1]))
        else:
            if queue != []:
                q_max = max(queue)
                q_min = min(queue)
                if tasks[1] == "-1":
                    queue.remove(q_min)
                else:
                    queue.remove(q_max)
            else:
                continue
    if queue == []:
        answer.append(0)
        answer.append(0)
    else:
        q_max = max(queue)
        q_min = min(queue)
        answer.append(q_max)
        answer.append(q_min)
    return answer
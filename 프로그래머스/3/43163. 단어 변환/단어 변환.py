class DFS:
    answer = 0
    def count_diff(self, word1, word2):
        length = len(word1)
        return sum([1 for i in range(length) if word1[i] != word2[i]])

    def run(self, n, words, now, target):
        if now == target:
            self.answer = n if self.answer == 0 else min(n, self.answer)
            return
        for w in words:
            if self.count_diff(now, w) == 1:
                temp = words.copy()
                temp.remove(w)
                self.run(n+1, temp, w,target)

def solution(begin, target, words):
    d = DFS()
    d.run(0, words, begin, target)
    return d.answer
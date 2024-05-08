class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        lenScore = len(score)
        answer = [0] * lenScore
        maxHeap = []
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        for index, s in enumerate(score):
            heappush(maxHeap, (-s, index))

        number = 1
        while maxHeap:
            s, index = heappop(maxHeap)
            if number < 4:
                answer[index] = rank[number - 1]
            else:
                answer[index] = str(number)
            number += 1
        return answer

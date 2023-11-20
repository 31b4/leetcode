class Solution:
    def countLetters(self, S: str) -> int:
        count = total = 1
        for i in range(len(S)-1):
            if S[i] == S[i+1]:
                count += 1
            else:
                count = 1
            total += count
        return total

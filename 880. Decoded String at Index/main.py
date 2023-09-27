class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        pattern = r'([a-zA-Z]+)(\d*)'
        matches = re.findall(pattern, s)
        result = [(match[0], int(reduce(lambda x, y: int(x) * int(y) if y else int(x), match[1], 1))) for match in matches]
        total_size = 0

        for word, times in result:
            total_size+=len(word)
            total_size *= times

        for word, times in result[::-1]:
            total_size //= times
            k %= total_size
            for x in word[::-1]:
                if k == 0 or k == total_size:
                    return x
                total_size -=1

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hm = Counter(arr).values()
        return len(set(hm))==len(hm)

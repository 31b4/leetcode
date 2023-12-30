class Solution:
    def makeEqual(self, w: List[str]) -> bool:
        return all(f%len(w)==0 for f in Counter(chain(*w)).values())

class Solution:
   def minCost(self, costs):
    prev = [0] * 3
    for now in costs:
        prev = [now[i] + min(prev[:i] + prev[i+1:]) for i in range(3)]
    return min(prev)

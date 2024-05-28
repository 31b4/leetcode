class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res: int = 0
        cur_cost: int = 0
        cur_start: int = 0

        for last_ind in range(len(s)):
            cur_cost += abs(ord(s[last_ind]) - ord(t[last_ind]))

            while cur_cost > maxCost:
                cur_cost -= abs(ord(s[cur_start]) - ord(t[cur_start]))
                cur_start += 1

            if last_ind - cur_start + 1 > res:
                res = last_ind - cur_start + 1

        return res

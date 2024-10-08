class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], 
                     coins: List[int]) -> List[int]:
        
        ans = []
        monsters, coins = zip(*sorted(zip(monsters, coins)))  # <-- 1.

        pref = list(accumulate(coins, initial = 0))           # <-- 2.

        for hero in heroes:                                   # <-- 3.
            ans.append(pref[bisect_right(monsters, hero)])    #
        
        return ans

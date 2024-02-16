class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cntr = Counter(arr)
        set_arr = set(arr)
        least_common_to_most = sorted(cntr, key=lambda x: cntr[x])
        i = 0

        while k > 0:
            if cntr[least_common_to_most[i]] <= k:
                set_arr.remove(least_common_to_most[i])
                k -= cntr[least_common_to_most[i]]
                i += 1
            else:
                break

        return len(set_arr)

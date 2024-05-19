class Solution:
    def maximumValueSum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        n: int = len(nums)
        temp: list[list[int]] = [[-1 for _ in range(2)] for _ in range(n)]  # temp[current_index(node)][is_even]

        def calculate_max(cur_ind, is_even) -> int:  # cur_ind -> cur_index of the tree and is_even represents whether we have already changed (XOR) even or odd number of nodes 
            if cur_ind == n:  # if we go to node which doesn't exist
                return 0 if is_even else -float("inf")
            if temp[cur_ind][is_even] != -1:  # if we've already encountered this state
                return temp[cur_ind][is_even]

            # checking all possible variants (no XOR or XOR)
            no_xor = nums[cur_ind] + calculate_max(cur_ind + 1, is_even)  # we don't change the number of XOR nodes
            with_xor = (nums[cur_ind] ^ k) + calculate_max(cur_ind + 1, not is_even)  # we added 1 XORed node

            mx_possible = max(no_xor, with_xor)
            temp[cur_ind][is_even] = mx_possible
            return mx_possible

        return calculate_max(0, 1)  # is_even == 1 because we have XORed 0 nodes which is even

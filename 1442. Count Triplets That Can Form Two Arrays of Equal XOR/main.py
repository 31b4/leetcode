class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        res = 0

        for start in range(len(arr) - 1):
            xor_first_arr = 0  # from start XOR for every subarray is 0

            for second_start in range(start + 1, len(arr)):
                xor_first_arr ^= arr[second_start - 1]  # count last character to previous XOR

                xor_second_arr = 0  # from start XOR for every subarray is 0
                for end in range(second_start, len(arr)):
                    xor_second_arr ^= arr[end]  # count character before end to previous XOR

                    if xor_first_arr == xor_second_arr:  # if XORes are equal
                        res += 1

        return res

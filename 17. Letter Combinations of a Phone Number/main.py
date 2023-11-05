class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def solve(combi, digits):
            if not digits:
                return [combi]

            results = []
            for letter in phone[digits[0]]:
                results.extend(solve(combi + letter, digits[1:]))

            return results

        return solve("", digits)

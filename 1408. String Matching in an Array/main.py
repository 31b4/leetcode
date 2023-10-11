class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = [] # we gonna store the results here

        for i, x in enumerate(words):
            # Join all words before and after the current word into a single string
            other_words = " ".join(words[:i] + words[i + 1:])
            # Example: words = ["mass","as","hero","superhero"]
            # other_words = "mass as hero superhero"

            # Check if the current word is a substring of other_words (any other words in words)
            if x in other_words:
                ans.append(x)

        return ans

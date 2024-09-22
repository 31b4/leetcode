class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = {}

        def insert(word):
            node = trie
            is_candidate = True
            for idx, ch in enumerate(word):
                if ch not in node:
                    if idx != len(word) - 1:
                        is_candidate = False
                    node[ch] = {}
                elif 'is_word' not in node[ch]:
                    is_candidate = False
                node = node[ch]
            node['is_word'] = True
            return is_candidate
        

        words.sort()
        max_len = 0
        result = ""
        for word in words:
            w_size = len(word)
            is_candidate = insert(word)
            if is_candidate and w_size > max_len:
                result = word
                max_len = w_size
        return result

        


        

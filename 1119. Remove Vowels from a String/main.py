class Solution:
    def removeVowels(self, s: str) -> str:
        return re.sub('[aeiou]', '', s)
        return re.subn("a|e|i|o|u", "", s)[0]
        return ''.join(c for c in S if c not in 'aeiou')
        return ''.join(list(filter(lambda x:x not in 'aeiou',S)))
        return s.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')

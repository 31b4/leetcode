class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        r = []
        # number of words
        self.wcnt = len(words)
        # length of each word
        self.wlen = len(words[0])
        # multiset of the original words
        self.wset = Counter(words)
        # length of the whole word sequence
        self.nseq = self.wlen * self.wcnt
        # checksum of the entire word sequence
        self.wcrc = sum([self.checksum(w) for w in words])
        for i in range(0, len(s) - self.nseq + 1):
            if (s[i : i + self.wlen] in self.wset
                # first check the checksum of the sequence
                and self.wcrc == self.checksum(s, i)
                # then verify if it's not a false positive
                and self.verify(s, i)):
                # add the current index to the result
                r.append(i)
        return r

    def checksum(self, s: str, idx: int = 0):
        # Calculate a simple checksum of the sequence
        # starting at the index idx until nseq or end of string
        checkSum = 0
        length = self.nseq if len(s) > self.nseq else len(s)
        for i in range(idx, idx + length):
            checkSum += ord(s[i])
        return checkSum

    def verify(self, s, i) -> bool:
        # verify that the multiset contains exactly the same items
        return self.wset == Counter(s[i + j : i + j + self.wlen] for j in range(0, self.wlen * self.wcnt, self.wlen))

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        hashT = {' ': ' '}
        i=97
        for k in key:
            if k not in hashT and k is not ' ':
                hashT[k] = chr(i)
                i+=1
        return "".join(hashT[m] for m in message)

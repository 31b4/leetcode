class Solution:
    def defangIPaddr(self, addr: str) -> str:
        return addr.replace(".","[.]")

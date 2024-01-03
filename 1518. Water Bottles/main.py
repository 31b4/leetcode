class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles

        while numBottles >= numExchange:
            newBottles = numBottles // numExchange
            res += newBottles
            numBottles = newBottles + numBottles % numExchange

        return res


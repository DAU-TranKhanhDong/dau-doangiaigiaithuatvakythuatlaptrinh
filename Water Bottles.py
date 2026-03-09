class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        total = 0
        empty = 0
        
        while numBottles > 0:
            total += numBottles
            empty += numBottles
            numBottles = empty // numExchange
            empty = empty % numExchange
        
        return total
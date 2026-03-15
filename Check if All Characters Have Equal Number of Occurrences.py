class Solution(object):
    def areOccurrencesEqual(self, s):
        count = {}
        
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        
        freq = count.values()
        first = freq[0]
        
        for v in freq:
            if v != first:
                return False
        
        return True
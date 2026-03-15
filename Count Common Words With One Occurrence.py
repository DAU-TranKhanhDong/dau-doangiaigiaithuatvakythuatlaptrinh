class Solution(object):
    def countWords(self, words1, words2):
        count1 = {}
        count2 = {}
        
        for w in words1:
            count1[w] = count1.get(w, 0) + 1
        
        for w in words2:
            count2[w] = count2.get(w, 0) + 1
        
        result = 0

        for w in count1:
            if count1[w] == 1 and count2.get(w, 0) == 1:
                result += 1
        
        return result
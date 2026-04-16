class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}
        
        for char in s:
            if char in counts:
                counts[char]+=1
            else:
                counts[char]=1

        for i in range(len(s)):
            char = s[i]
            if counts[char]==1:
                return i
            
        return -1 
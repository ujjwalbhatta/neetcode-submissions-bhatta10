class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        substring = {}
        result = 0

        for right in range(len(s)):
            if s[right] in substring and substring[s[right]] >= left:
                left = substring[s[right]] + 1

    
            substring[s[right]] = right
            result = max(result, right - left + 1)

        return result
        

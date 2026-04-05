class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        hashmap = {}
        max_len = 0

        for right in range(len(s)):
            if s[right] in hashmap:
                hashmap[s[right]] += 1
            else:
                hashmap[s[right]] = 1
                
            max_count = max(hashmap.values())

            if (right - left + 1) - max_count > k:
                hashmap[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


            
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  
        count = {}
        for items in strs:
            key = "".join(sorted(items))
            if key in count:
                count[key].append(items)
            else:   
                count[key] = [items]

        return list(count.values())

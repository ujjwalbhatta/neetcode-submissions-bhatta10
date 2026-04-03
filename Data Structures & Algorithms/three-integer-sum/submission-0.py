class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        # triple nested loops
        for i in range(n):
            for j in range(i+1, n):       # j > i
                for k in range(j+1, n):   # k > j
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in result:   # avoid duplicates
                            result.append(triplet)

        return result

        
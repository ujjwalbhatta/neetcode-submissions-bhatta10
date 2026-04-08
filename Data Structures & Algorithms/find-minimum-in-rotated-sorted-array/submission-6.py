class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        startIndex = 0
        endIndex = len(nums) - 1
  
        while startIndex < endIndex:
            mid = (startIndex + endIndex) // 2

            if nums[mid] > nums[endIndex]:
                startIndex = mid + 1
            else:
                endIndex = mid
            
        return nums[startIndex]

        
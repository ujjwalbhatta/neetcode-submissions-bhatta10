class Solution:
    def search(self, nums: List[int], target: int) -> int:
        startIndex = 0
        endIndex = len(nums) - 1

        while startIndex <= endIndex:
            midIndex = (startIndex + endIndex) // 2

            if nums[midIndex] == target:
                return midIndex

            if nums[startIndex] <= nums[midIndex]:
                if nums[startIndex] <= target <= nums[midIndex]:
                    endIndex = midIndex - 1
                else:
                    startIndex = midIndex + 1
            else:
                if nums[endIndex] >= target >= nums[midIndex]:
                    startIndex = midIndex + 1
                else:
                    endIndex = midIndex - 1

        return -1

            

                


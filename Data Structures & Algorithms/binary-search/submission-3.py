class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if (len(nums)<1): return -1

        middleIndex = len(nums)//2
        print(middleIndex, nums[middleIndex])

        if (nums[middleIndex]==target): return middleIndex

        elif (nums[middleIndex]>target): return self.search(nums[:middleIndex], target)

        else:
            result = self.search(nums[middleIndex+1:], target)
            return -1 if result == -1 else middleIndex + 1 + result

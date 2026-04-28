class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = set()

        #iterate through array
        for num in nums:
            if num in visited:#O(1)
                return True #
            visited.add(num)#O(1)

        return False
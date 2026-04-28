class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = set()

        #iterate through array, worst case scenario we iterate n times, so o(n)
        for num in nums:
            if num in visited:#O(1)
                return True 
            visited.add(num)#O(1)

        return False
        #worst case scenario we add n elements to the set, so space complexity is o(n)
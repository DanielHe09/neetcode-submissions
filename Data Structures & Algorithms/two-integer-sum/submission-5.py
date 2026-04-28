class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #create a hashmap of the list, key is the number, value is the number's index in the list
        my_hashmap = {}
        for i in range(0, len(nums)):#loop is o(n) time, the hasmap takes o(n) space
            my_hashmap[nums[i]] = i

        #iterate through list
        for i in range(0, len(nums)):#loop is o(n) time
            if ((target-nums[i]) in my_hashmap):
                if (i!=my_hashmap[target-nums[i]]):
                    return [i, my_hashmap[target-nums[i]]]
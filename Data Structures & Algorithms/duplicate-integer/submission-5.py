class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ##make a hash set, compare the length of the hashset to the original array. Based on result, return true or false
        hash_set = set()
        hash_set.update(nums)
        if len(nums) > len(hash_set):
            return True
        else:
            return False

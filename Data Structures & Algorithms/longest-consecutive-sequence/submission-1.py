class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet= set(nums) ##add nums into our set
        longest = 0

        for n in nums:
            if (n-1) not in numSet: ##check if there is no left neighbor, if not then it is beginning of sequence 
                length = 0
                while (n + length) in numSet: ##if there  is a right neighbor then keep going down our sequence
                    length += 1
                longest = max(length, longest) ##update our sequence length
        return longest
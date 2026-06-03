class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ##logic is to store nums array inside the set, iterate through nums, check if it is the start of 
        ##the sequence by checking if n-1 is in the set or not, while n + length is in the set, then
        ##keep incrementing. Find the longest 

        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
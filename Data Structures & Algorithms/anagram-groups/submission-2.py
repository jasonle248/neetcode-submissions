
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list) ##charCount : array of anagrams
        for i in strs: ##loop over every string
            count = [0] * 26 #a ... z

            for c in i: ##loop over every char in the string
                count[ord(c) - ord("a")] += 1 ##finds the value of the letter in the string and updates the count by 1

            hashMap[tuple(count)].append(i)
        return list(hashMap.values())
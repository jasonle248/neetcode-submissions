class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])

            i = j + 1 + length
        return res 

##To encode the string, we have to make into the format # of char in strings combined with # at the beginning
##To decode the string, we have to create a res array with a pointer. Go through the entire encoded string, 
##have another pointer j where we look for the #, once we find the #, from i to j is where we get the int,
##add that length from after the # to the end of the string, add it to the result list and start at the next
##word, return res
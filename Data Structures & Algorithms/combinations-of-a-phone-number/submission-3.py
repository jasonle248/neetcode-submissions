class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ##implement the hashmap
        charToNum = {"2" : "abc", "3" : "def", "4" : "ghi", "5": "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}

        res = []

        def dfs(i, isChar):
            if len(isChar) == len(digits):
                res.append(isChar)
                return 

            for c in charToNum[digits[i]]:
                dfs(i + 1, isChar + c)

        if digits:
            dfs(0, "")
        return res
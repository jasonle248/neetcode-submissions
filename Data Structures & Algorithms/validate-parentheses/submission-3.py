class Solution:
    def isValid(self, s: str) -> bool:
        ##create a close to open hashmap, to match the closing parentheses with the open ones, if it matches
        ##pop it off the stack, if the stack is empty than return true 

        closeToOpen = {')' : '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
    
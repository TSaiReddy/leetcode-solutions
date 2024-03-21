# Store the opposite value in the stack eg:- for this '(' we need to push ')' to stack
# Make sure you only remove last element in the stack as stack works as LIFO


class Solution:
    def isValid(self, s):
        if len(s) % 2 != 0:
            return False

        bracket_map = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for char in s:
            if char in bracket_map:
                stack.append(bracket_map[char])
            else:
                if not stack or char != stack[-1]:
                    return False
                else:
                    stack.pop()

        return not stack


solution = Solution()
solution.isValid("()[]{}")
print(solution.isValid("([}}])"))

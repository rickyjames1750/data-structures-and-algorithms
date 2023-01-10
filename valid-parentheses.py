class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(':
                stack.append('(')
            if c == ')':
                if len(stack) == 0:
                    return False
                if stack[-1] != '(':
                    return False
                else: stack.pop()

            if c == '{':
                stack.append('{')
            if c == '}':
                if len(stack) == 0:
                    return False
                if stack[-1] != '{':
                    return False
                else:
                    stack.pop()
                if c == '[':
                    stack.append(']')
                if c == ']':
                    if len(stack) == 0:
                        return False
                    if stack[-1] != ']':
                        return False
                    else:
                        stack.pop()
                if len(stack) > 0:
                    return False
                else: 
                    return True
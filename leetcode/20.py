class Solution:
    def isValid(self, s: str) -> bool:
        braces_map = {'(': ')', '[': ']', '{': '}'}
        opening_braces_stack = []
        for brace in s:
            if brace in ('(', '[', '{'):
                opening_braces_stack.append(brace)
            else:
                if len(opening_braces_stack) and \
                braces_map[opening_braces_stack[-1]] == brace:
                    opening_braces_stack.pop()
                else:
                    return False
        return len(opening_braces_stack) == 0


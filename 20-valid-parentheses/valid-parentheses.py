class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openParen = ["(", "{", "["]
        closeParen = [")", "}", "]"]
        closeToOpen = {")":"(", "}":"{", "]":"["} # Maps closed parenthesis to its open equivalent

        for paren in s:
            if paren in openParen:
                stack.append(paren)
            else:
                closeParen = paren
                if stack and (stack[-1] == closeToOpen[closeParen]):
                    # Make sure that this close parenthesis has an open parenthesis to cancel it out
                    stack.pop()
                    continue
                else:
                    return False

        return len(stack) == 0
        
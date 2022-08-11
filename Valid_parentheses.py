







def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    close_s = {
        ')' : '(',
        '}' : '{',
        ']' : '['
        }
    stack = []

    for ch in s:
        if ch not in close_s:
            stack.append(ch)
        else:
            if not stack or stack.pop() != close_s[ch]:
                return False

    return True if not stack else False


s = "]"

print(isValid(s))
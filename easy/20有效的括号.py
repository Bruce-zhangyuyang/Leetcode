#思路： 按照栈的想法，一个一个括号消掉 万一消不掉就返回False
def isValid(s: str) -> bool:
    dic = {'(': ')', '{': '}', '[': ']'}
    c = []
    for i in range(len(s)):
        if s[i] in dic:
            c.append(s[i])
        elif len(c) == 0 or dic[c.pop()] != s[i]:
            return False
    if len(c) == 0:
        return True
    else:
        return False

s = "("
print(isValid(s))

# 思路：把里面的空格和其他非数字字符全部清除 然后变为小写 看是否为回文
def isPalindrome(s: str) -> bool:
    s = ''.join(filter(str.isalnum, s)).lower() # isalnum：判断字符只有数字和字符 isalpha:判断只有字符 isalnum:判断只有数字
    return s == s[::-1]
str.isalnum()

# s = "A man, a plan, a canal: Panama"
s = '0P'
print(isPalindrome(s))
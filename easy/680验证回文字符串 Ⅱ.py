def validPalindrome(s: str) -> bool:
    if s == s[::-1]: return True
    for i in range(len(s)-1):
        s_ = s.copy()


a = "abac"
print(validPalindrome(a))
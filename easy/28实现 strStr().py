def strStr(haystack: str, needle: str) -> int:
    if needle == '': return 0
    if needle in haystack:
        return haystack.index(needle)
    else: return -1



# haystack = 'hello'
# needle = 'll'
haystack = "aaaaa"
needle = "bba"
print(strStr(haystack, needle))
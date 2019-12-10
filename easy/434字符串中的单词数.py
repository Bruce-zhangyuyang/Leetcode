# 直接对句子切分 然后数个数

def countSegments(s: str) -> int:
    return len(s.split())


s = "Hello, my name is John"

print(countSegments(s))
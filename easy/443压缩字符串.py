# 思路：三个指针：一个是读的位置，一个是读的这个元素相同的最远的位置，还有一个是写进去的地址，每次写一个以后write就加1
from typing import List
# def compress(chars: List[str]) -> int:
#     anchor = write = 0
#     for read, c in enumerate(chars):
#         if read+1 == len(chars) or chars[read+1] !=c:
#             chars[write] = chars[read]
#             write += 1
#             if read>anchor:
#                 for i in str(read - anchor + 1):
#                     chars[write] = i
#                     write += 1
#             anchor = read + 1
#     return write

# 思路2：第一个元素赋值给c，循环，计数，只要和c相等，就赋值‘00’， 要是不相等，就把计数赋值进列表，将不相等的元素放进c
def compress(chars: List[str]) -> int:




chars = ["a","a","b","b","c","c","c"]
print(compress(chars))


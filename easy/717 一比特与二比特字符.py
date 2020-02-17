from typing import List
# 思路：先将最后一位删掉 然后再将前面进行分割处理 留下最后的二位或者一位或者没有 再进行判断
def isOneBitCharacter(bits: List[int]) -> bool:
    bits = bits[:-1]
    print(bits)
    while len(bits) >2:
        if bits[0] == 0:
            bits.remove(bits[0])
        elif bits[0] == 1:
            bits.remove(bits[0])
            bits.remove(bits[0])
    print(bits)
    if bits == [0, 1] or bits == [1]:
        return False
    else:
        return True


bits = [1, 1, 1, 0]
# bits = [1, 0, 0]
# bits = [0]
# bits = [1,0,1,0]
print(isOneBitCharacter(bits))
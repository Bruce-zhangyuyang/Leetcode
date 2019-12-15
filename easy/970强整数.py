from typing import List
# 思路：把x和y的所有平方小于bound的情况列出来，组合相加
def powerfulIntegers(x: int, y: int, bound: int) -> List[int]:
    import math
    x_b = int(math.log(bound, x)) + 1 if x != 1 else 1
    y_b = int(math.log(bound, y)) + 1 if y != 1 else 1
    x_list = []
    y_list = []
    for i in range(x_b):
        x_list.append(x**i)
    for j in range(y_b):
        y_list.append(y**j)
    print(x_list, y_list)
    bound_list = []
    for i in x_list:
        for j in y_list:
            if i + j <=bound:
                bound_list.append(i + j)
    return list(set(bound_list))

x = 2
y = 1
bound = 10
print(powerfulIntegers(x, y, bound))

from typing import List


def hasGroupsSizeX(deck: List[int]) -> bool:
    if len(deck)<=1 : return False
    set_ = []
    for i in list(set(deck)):
        set_.append(deck.count(i))
    set_ = sorted(set_)
    if set_[0]<2: return False

    for i in range(2, set_[0]+1):
        k = 0
        for j in set_:
            if j % i != 0:
                k+=1
        if k == 0 : return True
    return False


deck = [1]
a = hasGroupsSizeX(deck)
print(a)
from typing import List


# def findRadius(houses: List[int], heaters: List[int]) -> int:
#     if len(heaters) == 1:
#         return max(abs(houses[0]-heaters[0]),abs(houses[-1]-heaters[0]))
#
#     else:
#         heaters = sorted(heaters)
#         houses = sorted(houses)
#         dist = max(abs(heaters[0] - houses[0]), abs(houses[-1] - heaters[-1]))
#         for i in range(len(heaters)-1):
#             s = (heaters[i+1]-heaters[i])/2
#             if dist < s :
#                 dist = int((heaters[i+1]-heaters[i])/2)
#         dist = min(abs(houses[-1] - heaters[0]), abs(heaters[0] - houses[-1]), dist)
#         return dist



# def findRadius(houses: List[int], heaters: List[int]) -> int:
#     houses = sorted(houses)
#     heaters = sorted(heaters)
#     srt = max(abs(heaters[-1]-houses[0]), abs(heaters[-1]-houses[-1]))
#     for i in range(len(heaters)-1):
#         dist = max(abs(heaters[i]-houses[0]), abs(heaters[i]-houses[-1]))
#         if srt > dist:
#             srt = dist
#     return srt


def findRadius(houses: List[int], heaters: List[int]) -> int:
    set_ = []
    houses = sorted(houses)
    heaters = sorted(heaters)
    for i in houses:
        a = max(abs(i-houses[-1]),abs(i-heaters[0]), abs(i-heaters[-1]))
        for j in heaters:
            dist = abs(i-j)
            if dist<a:
                a = dist
        set_.append(a)
    dist = set_[0]
    for i in set_:
        if i >dist:
            dist = i
    return dist

houses = [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
heaters = [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]
a = findRadius(houses, heaters)

print(a)
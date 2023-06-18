import heapq
from itertools import permutations
import math
import re

"""
Given A, B, C, find any string of maximum length that can be created such that no 3 consecutive characters are same. There can be at max A 'a', B 'b' and C 'c'.

- aaabbcc is not correct
- aabbcc is correct

"""


def solution_1(a, b, c):
    num = math.ceil((a + b + c) / 2)
    str_val = a*'a'+b*'b'+c*'c'
    str_per = list(set(list(permutations(str_val))))
    temp_str, output_str = [], []
    val = ["".join(i) for i in str_per]

    for each in val:
        all_find_str = re.findall(r"([a-z])\1{2,}", each)
        if not all_find_str:
            output_str.append(each)
        else:
            all_find_str = re.findall(r"([a-z])\1{2,}", each[:num])
        if not all_find_str:
            temp_str.append(each[:num])

    if output_str:
        return output_str[0]
    else:
        return temp_str[0]


def solution_2(A, B, C):
    res = ''
    pq = []
    for v, k in [(A, 'a'), (B, 'b'), (C, 'c')]:
        if v > 0:
            heapq.heappush(pq, (-v, k))
    prev_k, prev_v = '', 0

    while pq:
        v, k = heapq.heappop(pq)
        v = -v
        if prev_v:
            heapq.heappush(pq, (-prev_v, prev_k))
            prev_k, prev_v = '', 0
        if res[-2:] == k * 2:
            if len(pq) == 0:
                break
            prev_v, prev_k = v, k
        else:
            if v > 0:
                res += k
                v -= 1
                heapq.heappush(pq, (-v, k))

    return res

print("Solution 1: ")

print(solution_1(0,0,0))
print(solution_1(0,0,1))
print(solution_1(0,0,3))

print(solution_1(0,1,4))
print(solution_1(0,1,5))
print(solution_1(0,1,8))

# print(solution_1(6,1,1))
# print(solution_1(10,-5,5))

print("\nSolution 2: ")

print(solution_2(0,0,0))
print(solution_2(0,0,1))
print(solution_2(0,0,3))

print(solution_2(0,1,4))
print(solution_2(0,1,5))
print(solution_2(0,1,8))

print(solution_2(6,1,1))
print(solution_2(10,-5,5))
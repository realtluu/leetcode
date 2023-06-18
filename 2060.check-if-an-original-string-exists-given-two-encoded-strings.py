#
# @lc app=leetcode id=2060 lang=python3
#
# [2060] Check if an Original String Exists Given Two Encoded Strings
#

# @lc code=start
class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        def cut(s):
            l = []
            for k, it in itertools.groupby(s, key=lambda c: c.isdigit()):
                sub = ''.join(it)
                l.append(sub)
            return l
        l1 = cut(s1)
        l2 = cut(s2)
        def count(d):
            d = [int(c) for c in d]
            if len(d) == 1:
                yield d[0]
            elif len(d) == 2:
                yield sum(d)
                yield 10 * d[0] + d[1]
            else:
                yield sum(d)
                yield 10 * d[0] + d[1] + d[2]
                yield d[0] + 10 * d[1] + d[2]
                yield 100 * d[0] + 10 * d[1] + d[2]
        m, n = len(l1), len(l2)
        def helper(i, j, x, y):
            min_c = min(x, y)
            x -= min_c
            y -= min_c
            return equ(i, j, x, y)
        
        @functools.lru_cache(None)
        def equ(i, j, x, y):
            if (i == m and not x) or (j == n and not y):
                return (i == m and not x) and (j == n and not y)
            if i < m and l1[i].isdigit():
                return any(helper(i + 1, j, x + op, y) for op in count(l1[i]))
            elif j < n and l2[j].isdigit():
                return any(helper(i, j + 1, x, y + op) for op in count(l2[j]))
            else:
                if x > 0 and x >= len(l2[j]):
                    return helper(i, j + 1, x - len(l2[j]), y)
                elif y > 0 and y >= len(l1[i]):
                    return helper(i + 1, j, x, y - len(l1[i]))
                else:
                    if i == m or j == n:
                        return False
                    min_len = min(len(l1[i]) - y, len(l2[j]) - x)
                    if l1[i][y: y + min_len] != l2[j][x:x + min_len]:
                        return False
                    if len(l1[i]) - y == len(l2[j]) - x:
                        return helper(i + 1, j + 1, 0, 0)
                    elif len(l1[i]) - y < len(l2[j]) - x:
                        return helper(i + 1, j, x + len(l1[i]), y)
                    else:
                        return helper(i, j + 1, x, y + len(l2[j]))
        return equ(0, 0, 0, 0)
            
        
# @lc code=end


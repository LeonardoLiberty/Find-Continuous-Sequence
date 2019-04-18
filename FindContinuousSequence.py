# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum <= 2:
            return []

        ret = []

        def dfs(ret, index, su, count):

            if index-count > tsum//2:
                return

            if su > tsum:
                return dfs(ret, index + 1 - count, index+1-count, 0)
            elif su == tsum:

                re = []
                for i in range(count, -1, -1):
                    re.append(index - i)
                if len(re) == 1:
                    return
                ret.append(re)
                return dfs(ret, index + 1 - count, index + 1 - count, 0)

            else:

                index += 1
                su += index
                count += 1
                dfs(ret, index, su, count)

        dfs(ret, 1, 1, 0)
        return ret


if __name__ == '__main__':
    t = Solution().FindContinuousSequence(9)
    print t
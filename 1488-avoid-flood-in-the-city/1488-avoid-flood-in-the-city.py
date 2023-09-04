class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        zeros, lakes, ans = [], {}, [-1]*len(rains)

        for i,j in enumerate(rains):
            if j in lakes:
                idx = bisect.bisect_left(zeros,lakes[j])
                if idx == len(zeros): return []
                ans[zeros[idx]] = j
                zeros.pop(idx)
                lakes[j] = i
            elif j == 0:
                zeros.append(i)
            else: lakes[j] = i

        for i in range(len(ans)):
            if rains[i] == 0 and ans[i] == -1:
                ans[i] = 1

        return ans
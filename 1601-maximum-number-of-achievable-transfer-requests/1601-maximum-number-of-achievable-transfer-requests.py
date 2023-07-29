class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        answer = 0
        indegree = [0 for _ in range(n)]

        def maxRequest(index, count):
            if(index == len(requests)):
                for i in range(n):
                    if(indegree[i]):
                        return
                nonlocal answer
                answer = max(answer, count)
                return

            indegree[requests[index][0]] -= 1
            indegree[requests[index][1]] += 1

            maxRequest(index + 1, count + 1)

            indegree[requests[index][0]] += 1
            indegree[requests[index][1]] -= 1

            maxRequest(index + 1, count)

        maxRequest(0, 0)

        return answer
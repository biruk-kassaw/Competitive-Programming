class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        temp = []
        answer = []
        for i in points:
            temp.append([i,(i[0]*i[0])+(i[1]*i[1])])
        def sorter(arr):
            return arr[1]
        temp.sort(key=sorter)
        for i in range(k):
            answer.append(temp[i][0])
        return answer

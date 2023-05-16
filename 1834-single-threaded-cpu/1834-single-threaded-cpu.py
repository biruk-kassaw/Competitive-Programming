class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i , task in enumerate(tasks):
            task.append(i)
        
        tasks.sort(key=lambda x: x[0])
        ans = []
        time = tasks[0][0]
        i = 0
        minheap = []
        while minheap or i < len(tasks):
            while i < len(tasks) and  time >= tasks[i][0]:
                heappush(minheap, [tasks[i][1], tasks[i][2]])
                i += 1
                
            if minheap:
                curTime, index = heappop(minheap)
                time += curTime
                ans.append(index)
                
            else:
                time = tasks[i][0]
            
        return ans
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=self.sorter)
        print(intervals)
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i-1][1]:
                mini = min(intervals[i][0],intervals[i-1][0])
                maxi = max(intervals[i][1],intervals[i-1][1])
                intervals.pop(i)
                intervals.pop(i-1)
                intervals.insert(i-1,[mini,maxi])
            else:  
                i += 1

                
        return intervals
    
    def sorter(self, elem):
        return elem[0]

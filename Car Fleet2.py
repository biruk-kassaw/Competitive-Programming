class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        temp_arr = []
        stack = []
        fleets = 0
        for i in range(len(position)):
            temp_arr.append([position[i], speed[i]])
        temp_arr.sort(key=self.sorter,reverse=True)
        for i in range(len(temp_arr)):
            temp_arr[i] = (target - temp_arr[i][0])/ temp_arr[i][1]
        for i in range(len(temp_arr)):
            fleet_add = True
            while stack and stack[-1] >= temp_arr[i]:
                fleet_add = False
                break
            if fleet_add:  
                fleets += 1
                stack.append(temp_arr[i])
        return fleets
        
    def sorter(self,item):
        return item[0]

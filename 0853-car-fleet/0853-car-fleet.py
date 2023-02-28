class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        temp = [[position[i],speed[i]] for i in range(len(speed))]
        temp.sort(key=lambda pos :pos[0])
        for i in range(len(temp)):
            temp[i] = (target-temp[i][0])/temp[i][1]
        print(temp)
        fleets = 1
        r = len(temp) - 1
        l = r - 1
        while r >= 0 and l >= 0:
            if temp[l] <= temp[r]:
                l -= 1
                continue
            fleets += 1
            r = l
            l = r-1
        return fleets
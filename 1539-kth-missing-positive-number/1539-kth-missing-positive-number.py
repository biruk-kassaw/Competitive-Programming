class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        a= 0
        b=len(arr)-1
        while a <= b:
            m= a+(b-a)//2
            if arr[m]-m-1 < k:
                a = m+1
            else:
                b = m-1
        return a+k
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = {}
        for i in nums:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1
        good_pairs = 0
        print(counter)
        for i in counter:
            good_pairs += (counter[i] * (counter[i] -1))//2
        return good_pairs
            
            
            

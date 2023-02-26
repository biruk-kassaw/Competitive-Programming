class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_s1 = Counter(s1)
        counter_s2 = {}
        left = 0
        for i in range(len(s2)):
            counter_s2[s2[i]] = counter_s2.get(s2[i],0) + 1
            
            if i >= len(s1)-1:
                if counter_s1 == counter_s2:
                    return True

                counter_s2[s2[left]] -= 1
                if counter_s2[s2[left]] == 0:
                    del counter_s2[s2[left]]
                left += 1
                                
        return False
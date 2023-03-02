class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        waiting_time = 0
        for i in range(len(tickets)):
            if tickets[i] >= tickets[k]:
                if i > k:
                    waiting_time += tickets[k] - 1
                else:
                    waiting_time += tickets[k] 
            else:
                waiting_time += tickets[i]
                
    
        return waiting_time
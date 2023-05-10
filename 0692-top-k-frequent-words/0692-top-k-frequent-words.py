class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = Counter(words)
        word_heap = []
        
        for word in word_count:
            heappush(word_heap, (-word_count[word], word))
        heapify(word_heap)
        
        ans = []
        for _ in range(k):
            ans.append(heappop(word_heap))
        
        ans = [word[1] for word in ans]
        
        return ans
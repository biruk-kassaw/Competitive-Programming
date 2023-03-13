class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        words_count = []
        for word in words:
            min_char = min(word)
            words_count.append(word.count(min_char))
        words_count.sort()
        
        res = []
        for query in queries:
            query_count = query.count(min(query))

            left = 0
            right = len(words_count) - 1

            while left <= right:
                mid = (right + left) // 2
                if words_count[mid] <= query_count:
                    left = mid + 1
                else:
                    right = mid - 1

            res.append(len(words_count) - left)

        return res
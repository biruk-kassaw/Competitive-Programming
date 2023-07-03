class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def calculate_score(word):
            return sum(score[ord(c) - ord('a')] for c in word)

        def get_bitmask(word):
            bitmask = 0
            for c in word:
                bitmask |= 1 << (ord(c) - ord('a'))
            return bitmask

        word_scores = [calculate_score(word) for word in words]
        letter_count = Counter(letters)
        max_score = 0

        for bitmask in range(1, 1 << len(words)):
            bitmask_score = 0
            bitmask_count = Counter()

            for i in range(len(words)):
                if bitmask & (1 << i):
                    bitmask_score += word_scores[i]
                    bitmask_count += Counter(words[i])

            valid = True
            for letter, count in bitmask_count.items():
                if count > letter_count[letter]:
                    valid = False
                    break

            if valid:
                max_score = max(max_score, bitmask_score)

        return max_score
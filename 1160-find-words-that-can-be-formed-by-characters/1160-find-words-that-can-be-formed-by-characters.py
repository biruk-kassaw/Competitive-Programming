class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charSet = Counter(chars)
        length = 0
        for word in words:
            wordC = Counter(word)
            isGood = True
            for char in wordC:
                if char not in charSet or wordC[char] > charSet[char]:
                    isGood = False
                    break
            if isGood:
                length += len(word)
        return length
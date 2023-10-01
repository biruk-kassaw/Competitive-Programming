class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        for i, word in enumerate(arr):
            arr[i] = word[::-1]
        return " ".join(arr)
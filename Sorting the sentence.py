class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split()
        sorted_s = len(arr)*[""]
        for word in arr:
            index = int(word[-1])
            sorted_s[index-1] = word[:len(word)-1]
        str1 = " "
        sorted_s = str1.join(sorted_s)
        print(sorted_s)
        return(sorted_s)

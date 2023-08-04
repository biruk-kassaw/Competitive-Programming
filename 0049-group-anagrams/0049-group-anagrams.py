class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {}
        res = []
        for word in strs:
            temp = ''.join(sorted(word))
            if temp in myMap:
                myMap[temp].append(word)
            else:
                myMap[temp] = [word]
        for key in myMap.keys():
            res.append(myMap[key])
        return res
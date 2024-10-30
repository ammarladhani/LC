class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lettersAndQuantitiesS = {}
        lettersAndQuantitiesT = {}
        for i in range(len(s)):
            lettersAndQuantitiesS.setdefault(s[i],0)
            lettersAndQuantitiesS[s[i]] +=1
            lettersAndQuantitiesT.setdefault(t[i],0)
            lettersAndQuantitiesT[t[i]] +=1
        return lettersAndQuantitiesS == lettersAndQuantitiesT
        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        maxlen=0
        store=set()
        for r in range(len(s)):
            while s[r] in store:
                store.remove(s[l])
                l+=1
            store.add(s[r])
            maxlen=max(maxlen,r-l+1)

        return maxlen
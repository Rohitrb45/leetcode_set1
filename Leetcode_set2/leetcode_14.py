class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out=""
        strs.sort()
        first=strs[0]
        last=strs[len(strs)-1]
        #print(first)

        for i in range(len(first)):
            if first[i]!=last[i]:
                break;
            out+=first[i]
        
        return out
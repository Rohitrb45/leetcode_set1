class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        map={")":"(","}":"{","]":"["}
        for c in s:
            if c in map:
                if st and st[-1]==map[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)
        return True if not st else False
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result=[]
        carry=0
        a,b= a.zfill(max(len(a),len(b))),b.zfill(max(len(a),len(b)))
        for i in range(len(a)-1,-1,-1):
            sum=carry+int(a[i])+int(b[i])
            result.insert(0,str(sum%2))
            carry=sum//2

        if carry:
            result.insert(0,str(1))

        return ''.join(result)
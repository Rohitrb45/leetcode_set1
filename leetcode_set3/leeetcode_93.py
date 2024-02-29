class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        addr=[]
        address=[]
        def isvalid(s,i,addr,address):
            if(len(addr)==4):
                if i==len(s):
                    address.append('.'.join(addr))

            else:
                for j in range(i+1,i+4):
                    next_int=s[i:j]
                    if (j<=len(s) and
                       0<=int(next_int)<=255 and
                       (next_int=='0' or not next_int.startswith('0'))):
                           addr.append(next_int) 
                           isvalid(s,j,addr,address)
                           addr.pop()
        isvalid(s,0,addr,address)
        return address
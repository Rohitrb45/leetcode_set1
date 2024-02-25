def combinationSum(candidates, target):
        out=[]
        def csum(i,curr,total):
            if total==target:
                print(curr)
                out.append(curr[:])
                return
            if i>=len(candidates) or total>target:
                return
            curr.append(candidates[i])
            csum(i,curr,total+candidates[i])
            curr.pop()
            csum(i+1,curr,total)

        csum(0,[],0)
        return out


# Example usage:
candidates = [2, 3, 6, 7]
target = 7
result = combinationSum(candidates, target)
print(result)
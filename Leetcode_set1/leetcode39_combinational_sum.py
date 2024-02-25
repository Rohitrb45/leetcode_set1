def combination_sum(candidates, target):
    def backtrack(start, target, path, result):
        if target == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                continue
            path.append(candidates[i])
            backtrack(i, target - candidates[i], path, result)
            path.pop()

    result = []
    candidates.sort()  # Sorting the candidates can help avoid duplicates
    backtrack(0, target, [], result)
    return result

# Example usage:
candidates = [2, 2, 3, 6, 7]
target = 7
result = combination_sum(candidates, target)
print(result)

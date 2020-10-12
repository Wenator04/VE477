def knapsack(Sum, nums):
    if sum(nums) < Sum:
        return None
    results = [[]]
    results += [None for i in range(Sum)]
    for i in range(len(nums)):
        subResults = []
        for j in range(Sum - nums[i] + 1):
            if not (results[j] == None) and (results[j + nums[i]] == None) and not (j in subResults):
                results[j + nums[i]] = results[j] + [nums[i]]
                subResults.append(j + nums[i])
            if not (results[Sum] == None):
                return results[Sum]
    return results[Sum]

if __name__ == '__main__':
    Sum = int(input())
    nums = list(map(int, input().split()))
    results = knapsack(Sum, nums)
    if results == None:
        print()
    else:
        results.sort()
        print(results)

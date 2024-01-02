def pipe_fix(nums):
    result = []
    finish = nums[nums.__len__() - 1]
    for i in range(nums[0], finish + 1):
        result.append(i)
    return result

print(pipe_fix([1, 2, 3, 5, 6, 8, 9]))
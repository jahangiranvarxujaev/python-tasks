def findMaxConsecutiveOnes(nums):
    nums.append(0)
    count = 0
    compare_list = []
    for i in nums:
        if i == 1:
            count += 1
        else:
            compare_list.append(count)
            count = 0
    print(compare_list)
    return max(compare_list)
print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
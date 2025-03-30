def countTargetPairs(nums, target):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] < target:
                count += 1
    return count

# Test cases

nums1 = [-1, 1, 2, 3, 1]
target1 = 2
print("Test case 1:" + str(countTargetPairs(nums1, target1)))

nums2 = [-6, 2, 5, -2, -7, -1, 3]
target2 = -2
print("Test case 2:" + str(countTargetPairs(nums2, target2)))
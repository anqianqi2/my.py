'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。
示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
'''


def findMedianSortedArrays(num1,num2):
    num =sorted(num1 + num2)
    print(num)
    l = len(num)
    if l % 2 == 0:
        print(l/2)
        print(l/2 - 1)
        median = (num[int(l/2)] + num[int(l/2 - 1)])/2

    else:
        median = num[l//2]

    return median



if __name__ == '__main__':
    num1 = [1,3,8,9,8]
    num2 = [2,5,6,7,8,4,6]

    print(findMedianSortedArrays(num1,num2))



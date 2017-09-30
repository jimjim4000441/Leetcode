"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
"""

def twoSum( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    mydict = {} # store num:index
    for i in range (len(nums)):
        x = nums [i]
        y = target - x
        if y in mydict.keys():
            return  [mydict[y], i]
        mydict[x] = i
    return [-1]

#test code
if __name__ == '__main__':
    testdata = [
        [[1,2,3], 3, [0,1]],
        [[3, 7, 9, 10] , 19, [2, 3]],
        [[3,3,0], 6, [0,1]],
        [[3,4,7], 12, [-1]]
        ]
    for i in testdata:
        result = twoSum(i[0], i[1])
        assert result == i[2]
        print str(result) + "  Expected:   "+ str(i[2])

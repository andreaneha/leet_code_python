"""
note: typecasting a list!!


problem - Two Sum
--------------------------------------------

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

class Solution(object):
    def twoSums(self, nums, target):
        print("nums: " + " ".join(str(x) for x in nums)) #####interesting code
        print('target:' + str(target))

        # actual code
        numLen = len(nums)
        for currentIndex in range(numLen):
            for eachIndex in range(numLen):
                if currentIndex != eachIndex:
                    testSum = nums[currentIndex] + nums[eachIndex]
                    if testSum == target:
                        answer = [currentIndex, eachIndex]
                        return answer

        return[-1, -1]

#test harness
answer = Solution()
retAnswer = answer.twoSums([2,7,11,15], 9)
print("returned: " + " ".join(str(x) for x in retAnswer))


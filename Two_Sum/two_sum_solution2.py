"""
This solution uses a dictionary to make searching for the complement faster.

"""

class Solution(object):
    def twoSum(self, nums, target):
        index = 0;
        numDictionary = {} #initialize a blank dictionary
        for currentNum in nums:
            numDictionary[currentNum] = index #add domething to the dictionary. currentNum is the key and index is the value
            index+=1

        index = 0
        for currentNum in nums:
            compliment = target - currentNum
            if(compliment in numDictionary): #the in operator checks to see if the value on the left is in the value on the right
                compIndex = numDictionary.get(compliment) #get the value that goes with the compliment
                if(compIndex != index):
                    return [index, compIndex]
            index +=1
        return [-1, -1]

#test harness
answer = Solution()
retAnswer = answer.twoSum([3,3],6)
print("returned: " + " ".join(str(x) for x in retAnswer))

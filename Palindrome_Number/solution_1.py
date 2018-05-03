"""
Palindrome Number: https://leetcode.com/problems/palindrome-number/description/

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward. Also, don't convert the integer to a string

"""

class Solution(object):
    def isPalindrome(self,x):
        num = x
        checkNum = 0
        if(num == 0):
            return True
        if(num<0):
            return False
        
        while(num > 0):
            lastNum = num%10
            checkNum = (checkNum*10) + lastNum
            if(checkNum == 0):
                return False
            if(num == checkNum):
                return True
            num = (num-lastNum)/10
            if(num == checkNum):
                return True
        return False



#test harness
sol = Solution()
correctCounter = 0
if(not sol.isPalindrome(56075)):
    correctCounter+=1
if(sol.isPalindrome(5005)):
    correctCounter+=1
if(sol.isPalindrome(98389)):
    correctCounter+=1
if(sol.isPalindrome(4)):
    correctCounter+=1
if(not sol.isPalindrome(-70)):
    correctCounter+=1
if(not sol.isPalindrome(10)):
    correctCounter+=1
if(sol.isPalindrome(0)):
    correctCounter+=1
if(not sol.isPalindrome(220)):
    correctCounter+=1
if (correctCounter ==8):
    print("passed")


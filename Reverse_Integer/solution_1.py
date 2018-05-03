"""
Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 
Input: 123
Output: 321

Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [-2^31,  2^31 - 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

My solution converts the integer into a string, and then reverses it by using a pivot point and switching the values before and after it. After values get switched, the pivot expands and the loop repeats


"""

class Solution(object):
    def check32int(self, x):
        if(x<(-2**31) or x>=2**31):
            return False
        else:
            return True 
    def checkNeg(self, x):
        if(x<0):
            return True
        else:
            return False

    def reverseInt(self, x):
        neg = self.checkNeg(x)
        if(neg):
            x*=-1
        intstr = str(x)
        intlen = len(intstr)
        pivot = intlen/2
        if(intlen%2 == 0):
            newstr = ""
            startIndFl = pivot-1
            startIndCl = pivot
        else:
            newstr = str(intstr[intlen/2])
            startIndFl = pivot
            startIndCl = pivot
        for i in range(1, int(intlen/2) +1):
            newstr = intstr[startIndFl+i] + newstr
            newstr = newstr + intstr[startIndCl - i]
        if(neg):
            return int(newstr)*(-1)
        else:
            return int(newstr)


    def reverse(self, x):
        if (self.check32int(x)):
            newint = self.reverseInt(x)
            if(self.check32int(newint)):
                return newint
            else:
                return 0
        else:
            return 0



#test harness
#test check32int method
check32 = Solution()
if(not check32.check32int(2**64) and check32.check32int(6)):
    print("check function works")
else:
    print("check function does not work")
#check reverseInt method
checkRev = Solution()
newstr = checkRev.reverseInt(3069897)
print(newstr)
newstr = checkRev.reverseInt(306897)
print(newstr)
#check reverse method
newint = checkRev.reverse(6007)
print(newint)
newint = checkRev.reverse(2**40)
print(newint)
newint = checkRev.reverse(-567)
print(newint)

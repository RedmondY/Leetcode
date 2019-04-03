'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false

'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while i ** 2 <= num:
            if i ** 2 == num:  # 如果两个相等 则返回true
                return True
            else:
                i += 1
        return False


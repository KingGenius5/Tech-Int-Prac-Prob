'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

'''

'''
1. Restating the problem:
Basically I have to figure out whether an input reads the same forwards and backwards.
'''

'''
2: Ask Clarifying Questions
How many inputs could I get max?
Can I use built-in functions?
'''

'''
3: State Assumptions
The input will be an integer
'''

'''
4: Thinking Out Loud
Our solution will feature indexing.
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x)==str(x)[::-1]
        
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
Am I allowed to convert to a string right away?
What constitutes an edge case - single number, three of the same number?
'''

'''
3: State Assumptions
The input will be an integer.
Handle edge cases by throwing false.
Output is a boolean.
Numbers can be negative.
'''

'''
4: Thinking Out Loud
Right off the bat, I think of a quick and simple solution that happens to be a one-liner. Well, it can be a few lines depending on your variables.
Our solution will feature stepping. If we recall that slicers can take a third (optional) argument which sets the interval at which elements (in the list)
are included in the list, we can use this in our solution. Negative values (-1) reverses the direction in which the slicer iterates through the original list.
The indexed positions of the list elements don't change, but the order in which they're returned do. We can use this to compare it to the regular string (left side)
and see if they are equal. If they are, they will return True and be a Palindrome. One way you could improve this is limit the redundancy of the str conversions.
Also, another challenge would be to solve this problem without the use of str conversions.  
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x)==str(x)[::-1]
        
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

'''
1. Restating the problem:
So basically, I'm given a value and I have to choose two numbers in an array that add up to that value.
'''

'''
2: Ask Clarifying Questions
The example is great however does it account for negative numbers?
Is the array a fixed length?
Does the order of the list matter?
'''

'''
3: State Assumptions
A lot of assumptions were already stated but...
I can assume that there will be no duplicate integers
I can assume that the array will have no strings or floats
I can assume that the output will be one solution
'''

'''
4: Think Out Loud
The first way of going about it is through brute force and finding the naive solution. That would have us loop
through each element and find if there is another value that equals to x. But we can do a little better as that leaves
us with a time complexity of O(n^2). This is a O(n) solution that uses a dictionary to keep track of the values (it's better due to
dictionary's key value pairs) and return them as a list. Further solutions would need to be explored to reduce time complexity. Perhaps
an improvement would be tackling the problem in a different way in which we sort the numbers and split them in the middle to find the target
or otherwise perform a binary search.
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tested = {}
        
        for index, num in enumerate(nums):
            other = target - num
            
            if other in tested:
                return [tested[other], index]
            else:
                tested[num] = index
                
        return []
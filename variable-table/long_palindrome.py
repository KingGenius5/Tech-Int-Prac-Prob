"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Variable        |       Value
s               |       "babad"
m               |       "bab"
i               |       4
j               |       5
                |
return value    |       "bab"

"""

def long_pali(string):
    substr = ''
    for i in range(len(string)):
        for j in range(len(string), i, -1):
            if len(substr) >= j-i:
                break
            elif string[i:j] == string[i:j][::-1]:
                substr = string[i:j]
                break
    return substr

print(long_pali('babad'))

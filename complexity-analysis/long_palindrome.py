"""
Using the same example that was used for the variable tables, we can see here that this
function has a time complexity of O(n^2) due to its nested loops giving it a quadratic running time.
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

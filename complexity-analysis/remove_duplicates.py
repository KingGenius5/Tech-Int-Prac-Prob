"""
Using the same example that was used for the variable tables, we can see here that this
function has a time complexity of O(n) due to its singular loop resulting in linear running time.
"""

def find_duplicates(list):
    rep = {}
    for item in list:
        if item in rep:
            return item
        else:
            rep[item] = 1


if __name__ == "__main__":
    list = [0,2,2,3,4,5,7]
    print(find_duplicates(list))
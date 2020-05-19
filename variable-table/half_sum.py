"""
Given a positive integer n, calculate the following sum:

25  =>  25 + 12 + 6 + 3 + 1 = 47
        |   n       |   total       |   n>=1    |
        |     25    |       25      |   False   |
        |    12     |       37      |   False   |
        |     6     |       43      |   False   |
        |     3     |       46      |   False   |
        |   1       |       47      |   True    |
"""
def half_sum_factorial(num):
	total = num
	while num >= 1:
		num = int(num/2)
		total += num
	return total

print(half_sum_factorial(25))
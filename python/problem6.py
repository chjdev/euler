# Sum square difference
# Problem 6
# The sum of the squares of the first ten natural numbers is,
#
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


N = 100

nums = range(1, N + 1)
sum_nums = sum(nums)
sum_nums_squared = sum_nums ** 2

squared_nums = (num ** 2 for num in nums)
sum_squared_nums = sum(squared_nums)

print(sum_nums_squared, '-', sum_squared_nums, '=', sum_nums_squared - sum_squared_nums)

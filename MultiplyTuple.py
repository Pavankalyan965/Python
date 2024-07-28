def multiplyTuples(nums):
    Tuple = list(nums)
    mul = 1

    for a in Tuple:
        mul *=a
    return mul
nums = (1,3,56,78,94)
print(nums)
print(multiplyTuples(nums))
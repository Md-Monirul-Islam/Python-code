from functools import reduce
nums = [2,3,4,2]
nums_product = reduce((lambda x,y : x*y),nums)
print("The product of numbers : ",nums_product)

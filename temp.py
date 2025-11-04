def evenList(nums):
    # nums=[1,2,3,4]
    even = list(filter(lambda x:x%2==0,nums))
    return even

# print(evenList([1,2,3,4,56,67,8]))

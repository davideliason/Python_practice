def return_nums(nums):
    for num in nums:
        print(num)

def reverse_nums(nums):
    nums_to_print = []
    for num in nums:
        nums_to_print.append(num)
    return nums_to_print

print(reverse_nums([1,2,3]))
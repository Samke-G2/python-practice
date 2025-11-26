"""
Brief: Write a function that takes a lsit of numbers and returns the largest number.

author: Samke_G2

last edited: 26/11/2025     21:35
"""

def largestNum(nums):
    largest = nums[0]
    
    for i in nums:
        if i == largest:
            continue
        elif i > largest:
            largest = i
        else:
            continue
    
    return largest

tester = [2, 5, 4, 7, 8, 9, 2, 5, 7, 9, 0, 34, 23, 4, 53, 2, 24, 8, 45, 3, 25, 23]

print(largestNum(tester))
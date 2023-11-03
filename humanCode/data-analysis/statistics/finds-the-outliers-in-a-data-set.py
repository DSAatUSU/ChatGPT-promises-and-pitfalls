# Z score
import numpy as np

nums = input("Enter a list of numbers separated by spaces: ")
nums = [int(x) for x in nums.split()]

q75, q25 = np.percentile(nums, [75, 25])
iqr = q75 - q25

low = q25 - 1.5 * iqr
high = q75 + 1.5 * iqr

print("Outliers: ")
for x in nums:
    if x < low or x > high:
        print(x)

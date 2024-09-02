import numpy as np

nums1 = np.array([[2, 5, 2],[1, 5, 5]])
nums2 = np.array([[5, 3, 4],[3, 2, 5]])

print("Array1:") 
print(nums1)
print("Array2:") 
print(nums2)

print("\nMultiply said arrays of same size element-by-element:")
print(np.multiply(nums1, nums2))

import numpy as np

x = np.array([3,5,1,2,3])
y = np.array([2,5,3,2,1])

print("Array A")
print(x)
print("\nArray B")
print(y)

print("\nA>B")
print(np.greater(x, y))

print("\nA>=B")
print(np.greater_equal(x, y))

print("\nA<B")
print(np.less(x, y))

print("\nA<=B")
print(np.less_equal(x, y))



import numpy as np

x = np.arange(start=30, stop=71, step=2)
print(x)


import numpy as np

x = np.identity(3)
print(x)


import numpy as np

x = np.arange(21)
print("Vectors ")
print(x)

print("\nAfter changing the sign of the numbers in the range from 9 to 15:")
x[(x >= 9) & (x <= 15)] *= -1
print(x)


import numpy as np

x = np.diag([1, 2, 3, 4, 5])
print(x)


import numpy as np

x = np.array([[1,0],[0,1]])

print("Array")
print(x)

print("\nSum of all elements")
print(np.sum(x))

print("\nSum of each column")
print(np.sum(x, axis=0))

print("\nSum of each row")
print(np.sum(x, axis=1))



import numpy as np
import os

x = np.arange(16).reshape(4,4)

print("Array:")
print(x)

header = 'C1 C2 C3 C4'
np.savetxt('7_array.txt', x, fmt="%d", header=header)

print("\nAfter loading, content of the text file:")
print(np.loadtxt('7_array.txt'))


import numpy as np

nums1 = np.array([2,2,3,2,1])
nums2 = np.array([2,3,4,3,1])


print("Original arrays:")
print(nums1)
print(nums2)

print("\nTest said two arrays are equal (element wise) or not:?")
print(nums1 == nums2)
print(np.equal(nums1, nums2))


import numpy as np

nums = np.arange(16, dtype='int').reshape(-1, 4)
print("Original array:")
print(nums)

print("\nNew array after swapping first and last rows of the said array:")
#new_nums = nums[3:3:-1]

nums = nums[[-1,1,2,0]]
print(nums)

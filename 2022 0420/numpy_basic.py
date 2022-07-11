import numpy as np

#create array
np_array_1d = np.array([1,2,3]) 
print(type(np_array_1d))
print(np_array_1d.shape)
print(np_array_1d)

np_array_2d = np.array([[1, 2], [3, 4]]) 
print(type(np_array_2d))
print(np_array_2d.shape)
print(np_array_2d)
print(np_array_2d.ndim)
print(np_array_2d.size)

#asarray:
my_list = [1,2,3]
my_tuple = (1,2,3) 
numpy_a = np.asarray(my_tuple) 
numpy_b = np.asarray(my_list) 

print(numpy_a)
print(numpy_b)

np_array_zeros = np.zeros([3,4])
print(np_array_zeros)
np_array_ones = np.ones([2,3])
print(np_array_ones)
np_array_full = np.full([3,2], 5)
print(np_array_full)
np_array_eye = np.eye(3)   
print(np_array_eye)
np_random = np.random.random((3,2)) #0到1的隨機亂數
print(np_random)
np_arange = np.arange(4) # given number from 0~3
print(np_arange)
# for i in np.arange(4):
#     print(i)
#     df["fruit"][i]
np_linspace = np.linspace(0, 2*np.pi, 5) # given 5 value start from 0 in steps: 2pi
print(np_linspace)

#基本四則運算
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

# Elementwise sum; both produce the array
# [[ 6.0  8.0]
#  [10.0 12.0]]
print(x + y)
print(np.add(x, y))
print('==============')
# Elementwise difference; both produce the array
# [[-4.0 -4.0]
#  [-4.0 -4.0]]
print(x - y)
print(np.subtract(x, y))
print('==============')

# Elementwise product; both produce the array
# [[ 5.0 12.0]
#  [21.0 32.0]]
print(x * y)
print(np.multiply(x, y))
print('==============')

# Elementwise division; both produce the array
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print(x / y)
print(np.divide(x, y))
print('==============')

# Elementwise square root; produces the array
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print(np.sqrt(x))

#線性代數
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print(x.dot(y))
print(np.dot(x, y))
print('==============')

# Matrix transpose
print(x)
print(x.T)
print('==============')

# Matrix inverse
print(x)
print(np.linalg.inv(x))


#indexing
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

print(a[:2, 1:3])
print(a[:,2])

print(a[0, 1])   # Prints "2"
a[0, 1] = 77     # b[0, 0] is the same piece of data as a[0, 1]
print(a[0, 1])   # Prints "77

#reshape與 flatten

# b=np.arange(10000)
# b.reshape(-1,1000).shape
a.shape
a.reshape(2,6)
a.reshape(-1,2,3).shape
a.flatten().shape

#concatenate
a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
b = np.array([[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
print('Concatenate along axis=0:\n', np.concatenate((a,b), axis=0))
print('Concatenate along axis=1:\n', np.concatenate((a,b), axis=1))

#numpy.where()
lst = np.array([13, 4, 20, 15, 6, 20, 20])
result = np.where(lst == 20)
print(result)
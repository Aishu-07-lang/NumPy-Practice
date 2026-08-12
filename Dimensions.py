
#One dimension array
import numpy as np

x=[1,2,3,4,5,6]
y=np.array([1,2,3,4,5])
print(x)
print(y)
print(type(x))
print(type(y))
#To Check the Dimension
print(y.ndim)

# 2D array

ar2=np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(ar2)
print(type(ar2))
print(ar2.ndim)

#3D Array

ar3=np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
print(ar3)
print(type(ar3))
print(ar3.ndim)

#N Dimension Array
arn=np.array([1,2,3,4],ndim=10)
print(arn)
print(arn.ndim)
      





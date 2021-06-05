import numpy as np

#create Numpy array which consists of even numbers from 0 to 50
array = np.arange(0,51,2)
#create new array which consists of squared values of array
squaredArray = np.square(array)
#print array
print("Array : \n", array)
#print sum of the array
print("Sum of Array : \n", np.sum(array))
#print squared array
print("Squared Array : \n", squaredArray)
#print sum of the squared array
print("Sum of Squared Array : \n", np.sum(squaredArray))
#take the elements that are under 1000 with using Boolean masking method
print(squaredArray<1000)

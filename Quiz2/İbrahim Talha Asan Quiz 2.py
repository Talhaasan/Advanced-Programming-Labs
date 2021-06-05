import numpy as np
import math

number = input("Enter the number :")
#creating 0 array(array capacıty=number) 
array = np.zeros(int(number), dtype = int) 
print("Array : \n", array) 

def formulaOperation(array):#define function
    for number in range(len(array)):#apply formula and round operations.
        array[number] = np.round((((((1+math.sqrt(5))/2)**int(number)) -(((1-math.sqrt(5))/2) ** int(number))))/math.sqrt(5)) 
    print(array)
       
formulaOperation(array)#calling function

#for analysing and multiplying the array object
# munpy offer many ways to do array indexing:Slicing
import numpy as np

a1=np.array([[1,2,3,4,5,6,7],
             [8,9,10,11,12,13,14],
             [15,16,17,18,19,20,21],
             [22,23,24,25,26,27,28],
             [29,30,31,32,33,34,35]])
print("Array contents are \n",a1)

print(a1[2, 3])#displaying element at row-0, col-0

#slicing array1
s1=a1[0:3:1,0:4:1]
print("array with first 3 rows and first 4 columns:\n",s1)

#slicing array2
s2=a1[0:5:1,0:7:3]
print("array with first all rows and alternate columns:\n",s2)





























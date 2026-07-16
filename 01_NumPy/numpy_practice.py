#creating the  array 
# TOPIC1 :numpy arrays and matrix
import numpy as np
list1=[1,2,3,4,5,6]
oneD=np.array(list1)
print(oneD)

print(type(oneD)) #to find out what type

print(oneD.ndim) #to find the dimensions
print(oneD.shape) #to find out the element present in the array
#to create the two dimen
list2=[
    [1,2,4],
    [3,4,5,],
    [5,6,7]

]
twoD=np.array(list2)
print(twoD)

print(twoD.shape)

#conversion
#to convert the 1D to 2D  .reshape()
convertto2D=oneD.reshape(2,3)
print(convertto2D)


#to convert to 1d   #ravel()
convertto1D  = twoD.ravel()
print(convertto1D)

# to form the matrix  
matrix1 = np.matrix(list1)
print(matrix1)

matrix2=np.matrix(list2)
print(matrix2)

print(matrix2 * matrix2)

#Arithmetic Operatiosn in Array
# +, - , *, /
#
print(twoD + twoD)

print(oneD * oneD)

print(twoD * 3)  #broadcasting

#TOPIC2:Selecting Elements in Numpy Array
data1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
data2 = data1.reshape(5,5)
print(data2)

#to extract the element form 1D
print(data1[5])
print(data1[3:7])

#to extract the element from the 2D
#suppose we want [18,19],[13,14]
print(data2[1:3,2:4])       #------------arrayelement[rowseries:colseries]
                     #---------------rowseries= [startrowelement:endrowelement+1]
                     #---------------colseries= [startcolelement:endcolelement+1]
print(data2[1,2]) # for single element

#Fancy Indexing ---- (Extracting elements which are not in series)
#
# e.g. 7 , 14, 22 , 25
#
#
#      element       rowIndex      colIndex
#    ------------------------------------------
#         7             1             1
#         14            2             3
#         22            4             1
#         25            4             4
#
#

#  variableName[ rowIndexList, colIndexList]

print(data2[ [1,2,4,4] , [1,2,2,4]].reshape(2,2))

#Extract
#
#     7,8,9,
#     14,15,1
#     23,21,4
print(data2[[1,1,1,2,2,0,4,4,0],[1,2,3,3,4,0,2,0,3]].reshape(3,3))



#TOPIC: Logical Operations and Conditional Operations in Numpy
print(data2)

print(10 in data2) # to check the given  element present or not 

# Comparison Operators --->  >,<,>=,<=,!=,==
# Logical operators ------> and or not
#
# Use the following
#
# and ---- &
# or ----- |
# not ---- ~

print(data2 > 10) # to check elements greater than 10

print(data2[data2 > 15])  #return the values greater than 15

# Extract all values that are even number
print(data2[data2%2==0])

# Return those numbers greater than 11 and is an even number
print(data2[(data2>11) & (data2%2==0)])

#TOPiCS: Numpy_Initialiser_Functions  
#Initialization functions
# arange ------------- Generating arrays containing a sequence of numbers
# arange( start, stop(upperBoundValue) , step, dtype)
# uperBoundValue = end+1
print(np.arange(1,20))

print(np.arange(1,10,2))

print(np.arange(1,10,2,dtype=float))

print(np.arange(1,11).reshape(2,5))

#zeros and ones
print(np.zeros(10))
print(np.zeros(10,dtype=int))
print(np.ones(10))
print(np.ones(10).reshape(2,5))
print(np.zeros(10,dtype=int).reshape(2,5))


#Generate array with random numbers

# rand() ---- Returns random numbers which follow Uniform Distribution
#             (Uniform Distribution means the number will always be in the range of 0 and 1)

print(np.random.rand())

print(np.random.randn())   #Return random numbers that follow Normal Distribution
#                (Range of values will be such that the mean is 0 and stddev is 1)
# Random Integers

print(np.random.randint(1,10)) # Return me any integer value between 1 and 10

print(np.random.rand(1,1))
print(np.random.randint(1,10,5))  # Return 5 random integer values between 1 and 10

#identity matrix
print(np.eye(5))
print(np.eye(2,dtype=int))


#gussing game
n= int(input("enter the no between 1 to 15: "))
if n == np.random.randint(1,15):
  print("you won the game !!")
else:
  print("you lose the game, better luck next time..")
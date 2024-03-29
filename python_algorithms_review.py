"""
Python Algorithm Review
January 15th, 2024
Madeleine Lagerberg
Following this study guide: 
https://docs.google.com/document/d/1L2-8iQqpLyjIjdDsHzzdQ9X0GPwHS1SzGXDxk2FA7Eg/edit
"""

# import pandas as pd
import numpy as np
from time import time

### What is an algorithm: a step by step procedure to solve a computational problem.
# 1. Written during design phase
# 2. Domain expert writes - e.g. medical problem is defined by phsicians
# 3. Any language. Write paragraphs or mathematical notations
# 4. Independent of hardware and software
# 5. Analyze; study to find out if you are achieving the results and if it is efficient.

### What is a program: also a step-by-step procedure to solve a computational problem.
# 1. Written during implementation
# 2. Programmer writes
# 3. Programming language
# 4. Dependent on hardware and software
# 5. Testing; run-it and check it

#  First you design and then you implement. Start with english statements then build algorithm and construct the program.

### Priori Analysis and Posteriori Testing
# Priori Analysis: using deductive logic to construct an algorithm
# 1. Independent of language and hardware. 
# 2. Focus is on constructing accurate algorithm (time and space function).

# Posteriori Testing: using inductive logic (observational evidence) to understand actual performance
# 1. Depdendent on language and hardware.
# 2. Focus is on program optimization measured in time and bytes.

# 1. Input - 0 or more.
# 2. Output - must generate at least 1.
# 3. Definiteness - a single input must produce a single output.
# 4. Finiteness - must terminate at some point, duration must stop.
# 5. Effectiveness - like proof writing, any statement within an algorithm must be related to the algorthm objective/result.

# Process flow of an:
# Takes input
# As well defined instructions
# Executes on those instructions considering any inputs
# Provides at least one output

# Merriam-Webster defn:
# 1. Search Algorithm: a procedure that determines what kind of information is retrieved from a mass of data.
# 2. Encryption Algorithm: a set of rules by which information or messages are encoded so that unauthorized persons cannot read them.

### Characteristics of algorithm:
### 5 Basic Algorithms
# 1. Simple Recursive Algorithms
# 2. Algorithms within Data Structures
# 3. Divide & Conquer
# 4. Greedy Algorithms
# 5. Dynamic Programming

### Lesson 1: Simple Recursive Algorithms
# Recursion: a function that calls itself. That is, a function that is dependent on a previous output of that function.

## Exercise 1: Calculate a factorial using Last In First Out (LIFO) method.
num = 4

# My initial method (iterative approach)
def forFactorial(num):
    calcNum = num
    for i in range(1,num):
        # print(i)
        prevNum = num - i
        # print(prevNum)
        calcNum = calcNum * prevNum
        #print(calcNum)
    calcFactorial = calcNum
    #return print(calcFactorial)
    return calcFactorial

# With if statement (recursive)
def ifFactorial(num):
    if num == 1:
        return num
    else:
        temp = ifFactorial(num - 1)
        temp = temp * num
    return temp

# Readable recursive
def recur_factorial(num):
    if num == 1: return num
    else: return num * recur_factorial(num - 1)

# Execution time comparison shows the for loop is faster
startT = time()
forFactorial(600)
totalT = startT - time()
print(f'The time to run the for Factorial function is {totalT} seconds')

startT = time()
ifFactorial(600)
totalT = startT - time()
print(f'The time to run the for Factorial function is {totalT} seconds')

# Permutations: set of elements and find all combinations of those elements
# Swap the elements of a string (recursive method)
def permute(string, pocket=""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            # print(f'i = {i} \nletter = {letter} \nfront = {front} \nback = {back} \ntogether = {together} \npocket = {pocket} \n')
            permute(together, pocket + letter)

# permute("ABC","")
            
# print(permute("ABC", ""))
# string = "ABC"
# if string[0:0] == "":
#     print('same')

# Swap elements of a string (iterative method)
# def permute2(string):
#     for i in range(len(string)):
#         if i == 0:
#             letter = string[i]
#             permuteString = letter + string[i+1:]
#             print(permuteString)
#         else:
#             letter = string[i]
#             permuteString = string[i - 1] + letter + string[i + 1:]
#             print(permuteString)

# permute2("ABC")

def permutations(input_str):
    str = list(input_str)
    str.sort()
    for p in range(forFactorial(len(str))):
        print(''.join(str))
        i = len(str) - 1
        while i > 0 and str[i - 1] >= str[i]: # have to have >= to support strings with duplicate letters
            i -= 1
        str[i:] = reversed(str[i:])
        if i > 0:
            q = i
            while str[i - 1] >= str[q]: # have to have >= to support strings with duplicate letters
                q += 1
            temp = str[i - 1]
            str[i - 1] = str[q]
            str[q] = temp

s = 'hello'
s = list(s)
# permutations(s)
# s = list('abc')
# print(s)
# print(''.join(s))

### Write a function that takes a string as an input and returns the string reversed
def reverse_string(input_string):
    str = list(input_string)
    if str == []:
        print('Empty string, there is no reverse.')
    else:
        new_string = "" # start with empty string
        for i in range(len(str)):
            print(i)
            new_string += input_string[len(str) - 1 - i]
        print(new_string)
            # return new_string

reverse_string('')

### Write a function that finds the largest element in an array
# a = np.array([[-47,5,7,3,10], [5,48,2,192,4]])
a = np.array([[[-47,5,7,3,10], [5,48,2,972,4]], [[-47,5,7,3,10], [5,48,2,192,4]]])

print(a)
# print(a[0,0])
# print(a.ndim)
print(a.max()) # built in function that finds max integer
input_array = a
print(a.shape)
print(len(a.shape))
# print(len(input_array[0]))
# print(type(input_array[0]))

# Function to find largest element in an array
# for i in range(0, len(input_array.shape)):
#     print(f'testing {i}')
#     array_dim = input_array.shape[i] # iterate over dimensions of array
#     print(f'array dimension {array_dim}')
#     for j in range(0, array_dim): # iterate over elements of each dimension
#         print(input_array[i,j])
#         print(f'testing {i},{j}')


# print(a[1,1])

# for i in range(0,len(input_array.shape)): # iterate over the number of dimensions in our array
#     # while i > 0:
#         print(f'this is i: {i}')
#         for j in range(0,len(input_array.shape)):
#             print(input_array[i,j])

# for i in range(0,a.shape[0]):
#     print(i)
#     for j in range(0,a.shape[1]):
#         print(f'Positions {i} and {j}')
#         # print(a[i,j])
# print(f'testing 123 {input_array[1,1,0]}')


# for i in range(0,len(input_array.shape)):
#     print(i)
#     lst = list(input_array.shape)
#     for j in range(0, len(lst)):
#         print(f' this is my list {lst}')
#         print(f'this is the {j} element of my list {lst[j]}')
    # print(f'this is my array shape {lst}')
    # print(f'this is my list of elements for the array shape {lst[i]}')
    # print(f'this is the array element {input_array[i,i+1,i+2]}')


### ChatGPT solution
def find_largest_element(arr):
    # Check if the input array is empty
    if arr.size == 0:
        return None  # Return None for an empty array

    # If the input is a scalar (single element), return it
    if arr.ndim == 0:
        return arr.item()

    # Initialize the maximum value to negative infinity
    max_value = float('-inf')

    # Iterate through the elements in the NumPy array
    for element in np.nditer(arr):
        # If the element is greater than the current maximum, update max_value
        if element > max_value:
            max_value = element

    return max_value

# Example usage:
arr = np.array([[-47,5,7,3,10], [5,48,2,192,4]])
largest_element = find_largest_element(arr)
print("The largest element in the array is:", largest_element)
a = np.array([[[-47,5,7,3,10], [5,48,2,972,4]], [[-47,5,3837,3,10], [5,48,2,192,4]]])
largest_element = find_largest_element(a)
print("The largest element in the array is:", largest_element)

### Data structures review 
# Create a tree class and build a tree with a single node

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Creating a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)




"""
Python Algorithm Review
January 15th, 2024
Madeleine Lagerberg
Following this study guide: 
https://docs.google.com/document/d/1L2-8iQqpLyjIjdDsHzzdQ9X0GPwHS1SzGXDxk2FA7Eg/edit
"""

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

# My initial method: iterative approach
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

# With if statement
def ifFactorial(num):
    if num == 1:
        return num
    else:
        temp = ifFactorial(num - 1)
        temp = temp * num
    return temp

# Execution time comparison shows the for loop is faster
startT = time()
forFactorial(600)
totalT = startT - time()
print(f'The time to run the for Factorial function is {totalT} seconds')

startT = time()
ifFactorial(600)
totalT = startT - time()
print(f'The time to run the for Factorial function is {totalT} seconds')








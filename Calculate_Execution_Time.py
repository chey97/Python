# To calculate the execution time of the program, we need to calculate the time taken by the program from its initiation to the final result.
# 1. First, store the time of initiation of the program into a variable;
# 2. Write the Python program;
# 2. Store the end time of the program into a variable;
# 3. Subtract the time of initiation of the program from the end time of the program;

from time import time
start = time()

#Python Program to create acronyms
text = word = "Hello Programmers!"
text = word.split()
a = " "

for i in text:
    a = a + str(i[1]).upper()
print(a)

end = time()
execution_time = end - start
print("Execution time : ",execution_time)
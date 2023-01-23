# Given an array containing a range of numbers from 0 to n with a missing number, find the missing number in the input array.
# To find the missing number in an array, we need to iterate over the input array and store the numbers in another array that we didn’t find in the input array while iterating over it.

def findMissingNumbers(n):
    numbers = set(n)
    length = len(n)
    output = []
    
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output
    
listOfNumbers = [1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 14, 16, 17, 18, 21]
print(findMissingNumbers(listOfNumbers))

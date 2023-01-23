# Grouping elements of the same indices means grouping elements of two or more data structures according to their indices.
# To group elements of the same index, you will initially have two or more lists inside a list like [[a, b], [c, d]]. 
# To group the elements of these lists, you need to create two new lists where you will store the elements of both the lists at index 0 [a, c] and index 1 [b, d]. 
# That is the meaning of grouping the elements of the same indices.

inputList = [[10, 20, 30],[40, 50, 60],[70, 80, 90]]
outputList = []
index = 0

for i in range(len(inputList[0])):
    outputList.append([])
    for j in range (len(inputList)):
        outputList[index].append(inputList[j][ index]) # appends the element at the same index of each sublist in "inputList" to the corresponding list in "outputList"
    index = index + 1
a,b,c = outputList[0], outputList[1], outputList[2]
print(a,b,c)
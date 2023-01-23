#MEAN
list1 = [12, 16, 23, 23, 12, 30, 25, 24, 23, 20]
mean = sum(list1)/len(list1)
print(mean)

#MEDIAN
list1 = [12, 16, 23, 12, 45, 30, 25, 24, 23, 20]
list1.sort()

if len(list1) % 2 == 0:
    m1 = list1[len(list1)//2]
    m2 = list1[len(list1)//2 + 1]
    median = (m1 + m2)/2
else:
    median = float(list1[len(list1)//2])
    
print(median)

#MODE
list1 = [12, 16, 23, 12, 45, 30, 25, 24, 23, 20]
frequency = {}
for i in list1:
    frequency.setdefault(i,0)
    frequency[i]+=1
    
frequent = max(frequency.values())
for i, j in frequency.items():
    if j==frequent:
        mode=i
    
print(mode)
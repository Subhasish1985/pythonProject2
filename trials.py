'''

inputDetails = [3, 4, 6, 6, 7, 7, "Hello", "abc", "Hello", 3.4, 5.6, 3.4]
myUniqueList = []

for i in range(len(inputDetails)):

    #print(inputDetails[i])
    if inputDetails[i] not in myUniqueList:
        myUniqueList.append(inputDetails[i])


print(myUniqueList)


# The unique list of numbers is as follows :[3, 4, 6, 7, 'Hello', 'abc', 3.4, 5.6]
# The rejected list of numbers is as follows :[6, 7, 'Hello', 3.4]

list1 = [3, 4, 6, 7, 'Hello', 'abc', 3.4, 5.6]
list2 = [6, 7, 'Hello', 3.4]

for j in range(len(list1)):
    for y in range(len(list2)):

        if list1[j] == list2[y]:
            list1[j] = " "

print(list1)


for i in range(2.0):
    print(i)

X = "abcd"
for i in range(len(X)):
    print(i)


# prime numbers
for i in range(2, 11):
    for j in range(2, i):

        if i % j == 0:

            break
            #print("Not Prime", i)
            #break

        else:
            print("Prime", i)
            break






f = 1
A = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
for i in range(0, 3):
     f =f*i
     for j in range(0, 3):
         A[i][j] = f
print(A)



nums = set([1,2,3,4,5,4,3,2,1])
print(nums)


s={1,2,3,[4,5]}


list = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(list[])
'''




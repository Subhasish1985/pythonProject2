'''
Details:

Create a global variable called myUniqueList. It should be an empty list to start.

Next, create a function that allows you to add things to that list.
Anything that's passed to this function should get added to myUniqueList, unless its value already exists in myUniqueList.
If the value doesn't exist already, it should be added and the function should return True.
If the value does exist, it should not be added, and the function should return False;

Finally, add some code below your function that tests it out.
It should add a few different elements, showcasing the different scenarios, and then finally it should print the value of myUniqueList to show that it worked.


Extra Credit:

Add another function that pushes all the rejected inputs into a separate global array called myLeftovers.
If someone tries to add a value to myUniqueList but it's rejected (for non-uniqueness), it should get added to myLeftovers instead.

'''

myUniqueList = []  # to get the unique list of number
# inputDetails = [3, 4, 6, 6, 7, 7, 'Hello', 'abc', 'Hello', 3.4, 5.6, 3.4]
myduplicatelist = []  # to store the duplicate numbers
myLeftovers = []  # to store the duplicate numbers in a separate function
check = 0


def addValueTOList(inputDetails):
    for i in range(len(inputDetails)):

        # checking for unique numbers and adding it to the list
        if inputDetails[i] not in myUniqueList:

            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            myUniqueList.append(inputDetails[i])
            print("The first unique value '{}' has been added to the unique list and returning {}".
                  format(inputDetails[i], True))




        elif inputDetails[i] in myUniqueList:

            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            myduplicatelist.append(inputDetails[i])

            print(
                "The duplicate value '{}' has been added to the duplicate list and returning {}".format(inputDetails[i],
                                                                                                        False))

    # removing the values those duplicate to start with .Its optional.If this code is commented it returns the values of my myUniqueList
    for j in range(len(myUniqueList)):
        for y in range(len(myduplicatelist)):

            if myUniqueList[j] == myduplicatelist[y]:
                myUniqueList[j] = []

    return myUniqueList


enterValue = addValueTOList([3, 4, 6, 6, 7, 7, 'Hello', 'abc', 'Hello', 3.4, 5.6, 3.4])

print("                                                                                      ")
print("                                                                                      ")
print("{}{}".format("The unique list of numbers is as follows :", enterValue))


# Add another function that pushes all the rejected inputs into a separate global array called myLeftovers.

def rejectedInputs(myduplicatelist):
    myLeftovers = myduplicatelist
    # print("The duplicate value '{}' has been added and returning {}".format(inputDetails[i], False))
    return myLeftovers


leftovers = myduplicatelist
print("{}{}".format("The rejected list of numbers is as follows :", leftovers))

# print(myUniqueList)
# print(myduplicatelist)

# def pushDuplicate:

# returning True as 2 or more of the parameters are equal

def ifStatementValidation(firstNum, secondNum, thirdNum):
    if int(thirdNum) == secondNum or firstNum == int(thirdNum):  # returning True as 2 or more of the parameters are equal


        return print(True)

    elif firstNum != secondNum and firstNum != thirdNum:    # false is none of them are equal to any of the others.

        return print(False)


numValidate = ifStatementValidation(3, 5, "5")

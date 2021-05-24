'''
Details:

Create a function that takes in two parameters: rows, and columns, both of which are integers.
 The function should then proceed to draw a playing board (as in the examples from the lectures) the same number of rows and columns as specified.
  After drawing the board, your function should return True.


Extra Credit:

Try to determine the maximum width and height that your terminal and screen can comfortably fit without wrapping.
 If someone passes a value greater than either maximum, your function should return False.
'''

# Getting the size of the terminal
import shutil

size = shutil.get_terminal_size()  # to get the maximum width and height that the terminal

print(size)


# os.terminal_size(columns=80, lines=24)

def gameBoard(columns, lines):
    # checking the max value of the columns and line and returning false if greater than the max allowed value
    if columns > 80 and lines > 24:
        return print(False)

    for i in range(lines-1):  # goling through each rows starting from value 0
        if i % 2 == 0:  # checking if the row is of even number
            for j in range(1, columns):  # going through each column
                if j % 2 == 1:  # checking for odd number of columns
                    if j != columns - 1:  # to make sure the column is checked till the value of 79 , as max value of
                                            # coloumns in terminal is 80
                        print(" ", end="")  # until the column reaches it max value " " is printd in the same line
                    else:
                        print(
                            " ")  # once the value reaches the max value " " is printed and the control moves to the
                                    # next line
                else:
                    print("|", end="")  # on the odd value of the column '|' is printed
        else:
            print("-" * columns)  # at the end column in the new line , a line of '-' is created to the max value of 80

    return print(True)


valuePass = gameBoard(80, 24)

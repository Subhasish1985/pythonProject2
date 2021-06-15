# Adding each character of a number

number = int(input("Please enter a number: \n"))
sumEachCharacter = 0

while number != 0:
    sumEachCharacter = sumEachCharacter + (number % 10)
    number = int(number / 10)

    if sumEachCharacter > 9:
        sumEachCharacter = int((sumEachCharacter % 10) + (sumEachCharacter / 10))

print(sumEachCharacter)

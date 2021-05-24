'''
Details:

Return to your first homework assignments, when you described your favorite song.
Refactor that code so all the variables are held as dictionary keys and value.
Then refactor your print statements so that it's a single loop that passes through each item in the dictionary and
prints out it's key and then it's value.


Extra Credit:

Create a function that allows someone to guess the value of any key in the dictionary, and find out if they were right or wrong. This function should accept two parameters: Key and Value.
If the key exists in the dictionary and that value is the correct value, then the function should return true.
In all other cases, it should return false.

'''


songDetails = {'releaseDate': "February 1, 2017", 'Genre': "Arena rock&pop rock", 'songLengthInSecs': 204,
               'Producers': "Mattman & Robin"}

for key in songDetails:
   print(key , '->',songDetails[key])



def song_Details(key,value):
    if key in songDetails and songDetails[key]== value:
        return print(True)
    else:
        return print(False)

valueInput=song_Details('Genre','Aa rock&pop rock')

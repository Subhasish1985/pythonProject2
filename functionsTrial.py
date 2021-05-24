# implementing functions

# case 1: function to return the release date of the song


def songReleaseDate(release_date):
    print("The song was released on :")
    return release_date


release_date_value = songReleaseDate("February 1, 2017")
print(release_date_value)

# case 2 : function to return the genre of the song
genre1 = 'Arena rock'
genre2 = 'pop rock'


def songGenre(input1, input2):
    print("The song's genre are : ")

    return input1, input2


genre = songGenre(genre1, genre2)

print(genre)

# case 3  : total length of the song

songLengthInSecs = 204


def songDuration(totalDuration):
    print("The song's total length is :")

    return totalDuration


songLength = songDuration(204)
print(songLength)

# case 4 : Boolean

# boolT=True
# boolF=False
#name = 'Anthony'


def booleanTrial(boolT, boolF, inputName):
    if inputName == 'Anthony':

        return boolT

    elif inputName != 'Anthony':
        return boolF


boolean_return = booleanTrial(True, False, 'Anthony')

print(" Is tha name correct :")
print(boolean_return)

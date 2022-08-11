# 1. write the following functions
# 2. write a unittest class to test each of these functions once
# 3. Run it in this script

# Raising errors is more common when developing ------------------------

# These functions all take a single string as an argument.
# Presumably your code won't work for an int
# raise a built-in (or custom!) exception if fed an int
# make all characters capitalized
def shout(txt):
    try:
        return txt.upper()
    except AttributeError:
        if type(txt) in [int, float]:
            raise AttributeError("Cannot convert an integer or float")


# reverse all characters in string
def reverse(txt):
    try:
        return txt[::-1]
    except TypeError:
        if type(txt) in [int, float]:
            raise TypeError("Cannot convert an integer or float")


# reverse word order in string
def reversewords(txt):
    try:
        return ' '.join(txt.split()[::-1])
    except AttributeError:
        if type(txt) in [int, float]:
            raise AttributeError("Cannot convert an integer or float")


# reverses letters in each word
def reversewordletters(txt):
    try:
        return ' '.join(txt[::-1].split()[::-1])
    except TypeError:
        if type(txt) in [int, float]:
            raise TypeError("Cannot convert an integer or float")


# optional -- change text to piglatin.. google it!
# Doesn't handle punctuation well, but it works for most things
def piglatin(txt):
    try:
        return ' '.join((i[1:] + i[0] + "ay") for i in txt.split())
    except AttributeError:
        if type(txt) in [int, float]:
            raise AttributeError("Cannot convert an integer or float")


# Try/catch is more common when using
# someone else's code, scraping, etc. -----------------------------------

# Loop over this string and apply the reverse() function.
# Should throw errors if your exceptions are being raised!
# Write a try/catch to handle this.

stringList = ["hi", "hello there", 5, "hope this works", 100, "will it?"]

# for i in stringList:
#     shout(i)

# for i in stringList:
#     reverse(i)

# for i in stringList:
#     reversewords(i)

# for i in stringList:
#     try:
#         print(reversewordletters(i))
#     except TypeError:
#         pass

for i in stringList:
    try:
        print(piglatin(i))
    except AttributeError as err:
        print(err)

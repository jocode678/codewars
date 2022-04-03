# Write a function that takes in a string of one or more words, and returns the same
# string, but with all five or more letter words reversed (Just like the name of this Kata).
# Strings passed in will consist of only letters and spaces. Spaces will be included only when
# more than one word is present.
#
# Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
# spinWords( "This is a test") => returns "This is a test"
# spinWords( "This is another test" ) => returns "This is rehtona test"



# Splice string with space as delimitor and put into a list
def spinword(sentence):
    list = sentence.split(" ")
    print(list)
    newlist = []
    spinword = ""
    newsentence = ""

    for word in list:
        if len(word) >= 5:
            spinword = word [::-1]
            print(spinword)
            newlist.append(spinword)
        else:
            spinword = word
            print(spinword)
            newlist.append(spinword)
    newsentence = " ".join(newlist)
    return(newsentence)


sentence = "Hey fellow warriors"
print(spinword(sentence))

sentence = "This is a test"
print(spinword(sentence))

sentence = "This is another test"
print(spinword(sentence))




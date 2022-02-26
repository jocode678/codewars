# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
#
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

# def to_camel_case(text):
#     capsText = text.title()
#     interimresult = capsText.replace('-','')
#     result = interimresult.replace('_','')
#     return result


import re
def to_camel_case(text):
    if '_' in text:
        newtext = text.replace('_','-')
    else:
        newtext = text
    # slice into list
    list = newtext.split('-')
    # print(list)
    # Separate first item
    first = list.pop(0)
    # print(first)
    # print(list)
    # Convert list to string
    string = '-'.join(list)
    # print(string)
    # Convert to caps
    capsText = string.title()
    # print(capsText)
    # Replace dashes
    interimresult = capsText.replace('-', '')
    # print(interimresult)
    # Add first item back in and print result
    result = first + interimresult
    return result

text = 'i_am_jo'
print(to_camel_case(text))

text = 'i-am-jo'
print(to_camel_case(text))

text = 'i_am_coding'
print(to_camel_case(text))

text = 'i_am-mixing-symbols'
print(to_camel_case(text))

text = 'Starting-with-a-capital'
print(to_camel_case(text))

text = 'I_am-mixing-symbols'
print(to_camel_case(text))

# Need to make it so first character is not capitalised if not already

# text = 'i-am-jo'
# # slice
# list = text.split('-')
# print(list)
# # Separate first item
# first = list.pop(0)
# print(first)
# print(list)
# # Convert list to string
# string = '-'.join(list)
# print(string)
# # Convert to caps
# capsText = string.title()
# print(capsText)
# # Replace dashes
# interimresult = capsText.replace('-', '')
# print(interimresult)
# # Add first item back in and print result
# result = first + interimresult
# print(result)




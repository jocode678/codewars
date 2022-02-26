import re
def to_camel_case(text):
    if '_' in text:
        newtext = text.replace('_','-')
    else:
        newtext = text
    list = newtext.split('-')
    first = list.pop(0)
    string = '-'.join(list)
    capsText = string.title()
    interimresult = capsText.replace('-', '')
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
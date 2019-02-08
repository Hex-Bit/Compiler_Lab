# import re
# for getting more accurate output, converting the input file in one line. :)
with open('text.txt', 'r+') as f:
    contents = f.read()

    split_word = contents.split(' ')

# character_list = list(contents)

# print(character_list)

print(split_word)

keyword = ['int', 'float', 'string', 'double', 'if', 'byte', 'else', 'switch', 'else', 'return']
value = ["1", "2", "3", "4", "5", "6", "7", "8", "10"]
operator = ["-", "+", "/", "*"]
others = ["{", "}", ";", ")", "(", "[", "]", ",", ';']
logical_operator = ["<", ">", "&&", "||", "!=", "=="]
identifiers = ['a', 'b', 'c', 'd']

# Keyword
print('\n\nKeyWord = ', end='')
for word in split_word:
    for key in keyword:
        if word == key:
            print(word, end=' ')

# Identifiers
print('\n\nidentifiers = ', end='')
for word in split_word:
    for key in identifiers:
        if word == key:
            print(word, end=' ')

# value
print('\n\nvalue = ', end='')
for word in split_word:
    for key in value:
        if word == key:
            print(word, end=' ')

# others

print('\n\nothers = ', end='')
for word in split_word:
    for key in others:
        if word == key:
            print(word, end=' ')

# logical_operator

print('\n\nlogical_operator = ', end='')
for word in split_word:
    for key in logical_operator:
        if word == key:
            print(word, end=' ')

# operand

print('\n\noperator = ', end='')
for word in split_word:
    for key in operator:
        if word == key:
            print(word, end=' ')

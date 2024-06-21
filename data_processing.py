sentence = input('Enter a sentence: ')
sentence_formatted = sentence.upper()
print(str(sentence_formatted))

paragraph = input('Enter a paragraph: ').split()
paragraph_formatted = len(paragraph)
print(f'The number of words in this paragraph are: {paragraph_formatted}')

string = str(input('Enter a word: ')).isdigit()
print(f'All characters are digits: {string}')

string = input('Enter a word: ')
string_formatted = string.replace("a", "o")
print(f'Now you have your woooord, not waaard: {string_formatted}')

while True:
    name = input('Enter your name: ').upper()
    space_index = name.find(' ')

    if  space_index != -1:
        name_initial = name[0]
        lastname_initial = name[space_index + 1]
        number = "7"
        initials = name_initial + lastname_initial + number
        print(f'Your initials are: {initials}')
        break
    else:
        print(f'Introduce your name with a space')

string = str(input('Enter a word: '))
string_lenght = len(string)
print(f'The lenght of your string is : {string_lenght}')
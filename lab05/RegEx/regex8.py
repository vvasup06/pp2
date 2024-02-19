import re

def uppercase_letters(string):
    letters = re.findall(r'\w', string)
    uppercase_string = ' '.join(letter.upper() for letter in letters)
    return uppercase_string

input_string = input("Введите строку: ")
uppercase_string = uppercase_letters(input_string)
print("Строка с заглавными буквами:", uppercase_string)
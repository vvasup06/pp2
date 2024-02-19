import re

def replace_chars(string):
    pattern = r'[ ,.]' 
    replacement = ':'   
    modified_string = re.sub(pattern, replacement, string)
    return modified_string

text = input("Введите строку для проверки: ")
modified_text = replace_chars(text)
print("Измененная строка: ", modified_text)
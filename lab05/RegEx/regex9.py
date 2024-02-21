import re

def insert_spaces(text):
    result = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    return result

input_text = input("Введите текст: ")
text_with_spaces = insert_spaces(input_text)
print("Текст с пробелами перед словами, начинающимися с заглавной буквы:")
print(text_with_spaces)
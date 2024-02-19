import re

def insert_spaces(text):
    # Используем регулярное выражение для поиска всех слов, начинающихся с заглавной буквы
    # и вставки пробела перед каждым найденным словом
    result = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    return result

input_text = input("Введите текст: ")
text_with_spaces = insert_spaces(input_text)
print("Текст с пробелами перед словами, начинающимися с заглавной буквы:")
print(text_with_spaces)
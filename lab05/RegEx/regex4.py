import re

def find_sequences(text):
    pattern = r'[A-Z][a-z]+'
    sequences = re.findall(pattern, text)
    return sequences

text_to_search = input("Введите строку: ")
sequences_found = find_sequences(text_to_search)
print("Найденная5 строка: ", sequences_found)
import re

def find_sequences(text):
    pattern = r'[a-z]+(?:_[a-z]+)+'
    sequences = re.findall(pattern, text)
    return sequences

text_to_search = input("Введите строку: ")
sequences_found = find_sequences(text_to_search)
print("Найденные последовательности:", sequences_found)
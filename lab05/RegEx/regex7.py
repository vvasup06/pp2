import re

def convert_snake_to_camel(text):
    pattern = r'_(\w)' 
    camel_case = re.sub(pattern, lambda x: x.group(1).upper(), text)
    camel_case = camel_case.replace('_', '')
    return camel_case

text_to_search = input("Введите строку: ")
camel_case_string = convert_snake_to_camel(text_to_search)
print("Строка в верблюжьем регистре:", camel_case_string)
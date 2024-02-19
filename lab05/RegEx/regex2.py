import re 
def match_pattern(text):
    pattern = r'a*b{2,3}'
    match = re.fullmatch(pattern,text)
    if match:
        return True
    else:
        return False
text_to_match = input("Введите строку для проверки: ")
if match_pattern(text_to_match):
    print("Строка соответствует шаблону.")
else:
    print("Строка не соответствует шаблону.")
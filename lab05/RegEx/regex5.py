import re
def match_pattern(text):
    pattern = r'a.*b$'
    match = re.fullmatch(pattern,text)
    if match:
        return True
    else:
        return False
text_to_match = input("Введите строку для проверки: ")
if match_pattern(text_to_match):
    print("Строка соотвествует шаблону: ")
else:
    print("Строка не соотвествует шаблону: ")

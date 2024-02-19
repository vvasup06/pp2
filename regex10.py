import re

def convert_camel_to_snake(camel_case):
    snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case).lower()
    return snake_case

# Example usage:
camel_string = "camelCaseString"
snake_string = convert_camel_to_snake(camel_string)
print("Snake case:", snake_string) 
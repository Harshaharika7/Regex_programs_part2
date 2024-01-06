import re

def remove_integers(input_string):
    return re.sub(r'\d+', '', input_string)

original_string = "Hello123 World456!"
result = remove_integers(original_string)
print(result)

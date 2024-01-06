def remove_unwanted_spaces(input_string):
    return ' '.join(input_string.split())
original_string = "   This   is  an  example   with  apples   .   "
result = remove_unwanted_spaces(original_string)
print(result)

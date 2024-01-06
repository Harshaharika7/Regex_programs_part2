def find_capital_words(input_string):
    words = input_string.split()
    capital_words = [word for word in words if word[0].isupper()]
    return capital_words
sentence = "This is an Example Sentence with CAPITAL LETTERS"
result = find_capital_words(sentence)
print(result)

def print_upper_words(words, must_start_with):     
    """This function takes the list of words and uppercase the letters"""
    for word in words:
        if word.upper().startswith(tuple(letter.upper() for letter in must_start_with)):
            print(word.upper())

words = ["Hello", "Hey", "Yo", "Yes", "Enlargement", "Exercise", "extraction"]

print_upper_words(words, must_start_with={"h", "y"})
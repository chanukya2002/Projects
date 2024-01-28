def count_words(text):
    """
    Count the number of words in the given text.
    """
    words = text.split()
    return len(words)


print("Word Counter Program")

# User input
user_input = input("Enter a sentence or paragraph: ")

# Check for empty input
if not user_input:
    print("Error: Empty input. Please enter some text.")
    

# Count words
word_count = count_words(user_input)

# Display word count
print(f"\nWord Count: {word_count}")



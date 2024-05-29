import string


def count_words(text):
    """
    This function counts the number of words in a given text.
    Args:
    text (str): The input text.

    Returns:
    int: The word count.
    """
    # Remove punctuation from the text
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Split the text into words using whitespace as the delimiter
    words = text.split()
    # Return the number of words
    return len(words)


def main():
    """
    Main function to run the word counter program.
    """
    while True:
        # Prompt the user to enter a sentence or paragraph
        user_input = input(
            "Please enter a sentence or paragraph (or type 'exit' to quit): ").strip()

        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            print("Exiting the Word Counter program. Goodbye!")
            break

        # Check if the input is empty
        if not user_input:
            print("Error: No input provided. Please enter some text.")
            continue

        # Call the count_words function and get the word count
        word_count = count_words(user_input)

        # Display the word count to the user
        print(f"The number of words in the given text is: {word_count}\n")


# Ensure the main function runs when the script is executed
if __name__ == "__main__":
    main()

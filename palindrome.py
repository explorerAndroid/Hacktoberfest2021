def is_palindrome(text):
    removed_whitespace = text.replace(
        " ", ""
    ).lower()  # Removing whitespace from string and converting it to lower case
    reversed = removed_whitespace[
        ::-1
    ]  # Reversing the string and storing it in a separate variable

    if (
        removed_whitespace == reversed
    ):  # Checking if original text is equal to reversed text, if it is then it is palindrome, else not.
        print(f"Palindrome! {text} is a palindrome.\n")

    else:
        print(f"Not A Palindrome! {text} is not a palindrome.\n")


while True:
    text = input("Enter Some Text: \t")  # Taking input
    is_palindrome(text)  # Running the function

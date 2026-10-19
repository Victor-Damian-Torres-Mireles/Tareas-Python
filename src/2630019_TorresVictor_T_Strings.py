# ==============================================================================
# COVER
# ==============================================================================
# Name   : Victor Damian Torres Mireles
# ID     : 2630019
# Email  : 2630019@upv.edu.mx
# Group  : IM 1-1
# Course : Programming methodologies
# Teacher: M.C. Carlos Antonio Tovar Garcia
# GitHub : https://github.com/Victor-Damian-Torres-Mireles
# ==============================================================================




# ==============================================================================
# EXECUTIVE SUMMARY
# ==============================================================================
# A string in Python is a data type used to store text, and it is immutable.
# Basic string operations include concatenation, measuring length, extracting substrings,
# searching for patterns, and replacing text.
# Validating and normalizing input helps prevent errors and ensures consistent data.
# These practices are useful when processing emails, names, passwords, and other text.
# This document presents a description of each problem and its expected behavior.
# It explains the input and output design, the validations applied, and the string methods used.
# Each problem includes test cases and Python code to demonstrate the solution.
# ==============================================================================




# ==============================================================================
# PRINCIPLES AND GOOD PRACTICES
# ==============================================================================
# - Strings are immutable: any modification creates a new string.
# - It is good practice to normalize input with strip() and lower() before comparing it.
# - Avoid "magic numbers" in indexes and document what each slice extracts.
# - Use string methods instead of rewriting basic logic.
# - Design clear validations: first check that the input is not empty, then validate its format.
# - Write readable code using clear variable names and understandable error messages.
# ==============================================================================




# ==============================================================================
# Problem 1: Full name formatter (name + initials)
# ==============================================================================
# Description:
# Receives a person's full name in a single string.
# Normalizes spaces and capitalization, then displays
# the formatted name and its initials.
#
# Inputs:
# - full_name (string): The person's full name.
#
# Outputs:
# - Formatted name: Name in Title Case.
# - Initials: First letter of each word separated by dots.
#
# Validations:
# - The name cannot be empty or contain only spaces.
# - The name must contain at least two words.
# ==============================================================================
# Test cases:
# ==============================================================================
# 1) Normal: "victor torres mireles"
#    Output: Victor Torres Mireles / V.T.M.
# 2) Border: "   vICTOR  tORRes mIrelES   "
#    Output: Victor Torres Mireles / V.T.M.
# 3) Error: "   "
#    Output: Error: Invalid input
# ==============================================================================


# Ask the user to enter their full name and remove spaces at the beginning and end.
full_name = input("Enter your full name: ").strip()

# Split the full name into a list of words.
words = full_name.split()

# Check if the name contains fewer than two words.
if len(words) < 2:
    # Display an error message if the name has fewer than two words.
    print("Error: Invalid input")
else:
    # Join the words with a single space and capitalize the first letter of each word.
    full_name = " ".join(words).title()

    # Get the first letter of each word, convert it to uppercase, and separate the initials with periods.
    initials = ".".join(word[0].upper() for word in words) + "."

    # Display the formatted full name.
    print("Formatted name: ", full_name)

    # Display the initials of the full name.
    print("Initials: ", initials)


# ==============================================================================
# Problem 2: Simple email validator (structure + domain)
# ==============================================================================
# Description:
# Validates the basic structure of an email address.
# If the email is valid, it displays the domain.
#
# Inputs:
# - email_text (string): The email address entered by the user.
#
# Outputs:
# - "Valid email: true" or "Valid email: false"
# - If valid, "Domain: <domain_part>"
#
# Validations:
# - The email cannot be empty after strip().
# - The email must contain exactly one '@'.
# - There must be at least one '.' after the '@'.
# - The email cannot contain spaces.
# ==============================================================================
# Test cases:
# ==============================================================================
# 1) Normal: "user@gmail.com"
#    Output: Valid email: true
#            Domain: gmail.com
# 2) Border: "a@b.c"
#    Output: Valid email: true
#            Domain: b.c
# 3) Error: "user@@gmail.com"
#    Output: Valid email: false
# ==============================================================================


# Ask the user to enter an email address and remove spaces at the beginning and end.
email_text = input("Enter your email: ").strip()

# Check if the email is empty, does not contain exactly one @ symbol, or contains spaces.
if len(email_text) == 0 or email_text.count("@") != 1 or " " in email_text:
    # Display false if any of the initial validation conditions are met.
    print("Valid email: false")
else:
    # Find the position of the @ symbol in the email.
    at_position = email_text.find("@")

    # Extract the domain by taking the text after the @ symbol.
    domain_part = email_text[at_position + 1:]

    # Check if the domain contains a period.
    if "." in domain_part:
        # Display true if the email passes all the defined validations.
        print("Valid email: true")

        # Display the domain extracted from the email address.
        print("Domain: " + domain_part)
    else:
        # Display false if the domain does not contain a period.
        print("Valid email: false")



# ==============================================================================
# Problem 3: Palindrome checker
# ==============================================================================
# Description:
# Determines whether a phrase is a palindrome.
# It ignores spaces and uppercase/lowercase differences.
#
# Inputs:
# - phrase (string): The phrase to check.
#
# Outputs:
# - "Is palindrome: true" or "Is palindrome: false"
# - Normalized phrase.
#
# Validations:
# - The phrase cannot be empty after strip().
# - The normalized phrase must contain at least 3 characters.
# ==============================================================================
# Test cases:
# ==============================================================================
# 1) Normal: "Anita lava la tina"
#    Output: Is palindrome: true
# 2) Border: "aba"
#    Output: Is palindrome: true
# 3) Error: "  "
#    Output: Error: Invalid input
# ==============================================================================


# Ask the user to enter a phrase and remove spaces at the beginning and end.
phrase = input("Enter a phrase: ").strip()

# Convert the phrase to lowercase and remove all spaces.
normalized = phrase.lower().replace(" ", "")

# Check if the normalized phrase contains fewer than three characters.
if len(normalized) < 3:
    # Display an error message if the phrase is too short.
    print("Error: Invalid input")
else:
    # Reverse the normalized phrase by reading its characters from right to left.
    reversed_phrase = normalized[::-1]

    # Compare the normalized phrase with its reversed version.
    if normalized == reversed_phrase:
        # Display true if both strings are equal.
        print("Is palindrome: true")
    else:
        # Display false if both strings are different.
        print("Is palindrome: false")

    # Display the normalized phrase without spaces and in lowercase.
    print("Normalized phrase: " + normalized)


# ==============================================================================
# Problem 4: Sentence word stats
# ==============================================================================
# Description:
# Counts the words in a sentence and finds the first, last,
# shortest, and longest word.
#
# Inputs:
# - sentence (string): The sentence to analyze.
#
# Outputs:
# - Word count
# - First word
# - Last word
# - Shortest word
# - Longest word
#
# Validations:
# - The sentence cannot be empty after strip().
# - At least one valid word must exist after split().
# ==============================================================================
# Test cases:
# ==============================================================================
# 1) Normal: "Python is very useful"
#    Output: Word count: 4
# 2) Border: "Hello"
#    Output: Word count: 1
# 3) Error: "   "
#    Output: Error: Invalid input
# ==============================================================================


# Ask the user to enter a sentence and remove spaces at the beginning and end.
sentence = input("Enter a sentence: ").strip()

# Split the sentence into a list of words.
words = sentence.split()

# Check if the list contains no words.
if len(words) == 0:
    # Display an error message if the sentence is empty.
    print("Error: Invalid input")
else:
    # Set the first word as the initial shortest word.
    shortest_word = words[0]

    # Set the first word as the initial longest word.
    longest_word = words[0]

    # Go through each word in the list.
    for word in words:
        # Check if the current word is shorter than the shortest word found so far.
        if len(word) < len(shortest_word):
            # Update the shortest word with the current word.
            shortest_word = word

        # Check if the current word is longer than the longest word found so far.
        if len(word) > len(longest_word):
            # Update the longest word with the current word.
            longest_word = word

    # Display the total number of words in the sentence.
    print("Word count: " + str(len(words)))

    # Display the first word in the list.
    print("First word: " + words[0])

    # Display the last word in the list.
    print("Last word: " + words[-1])

    # Display the shortest word found.
    print("Shortest word: " + shortest_word)

    # Display the longest word found.
    print("Longest word: " + longest_word)



# ==============================================================================
# Problem 5: Password strength classifier
# ==============================================================================
# Description:
# Classifies a password as weak, medium, or strong.
#
# Rules:
# - Weak: length is less than 8, contains only lowercase letters,
#   or consists of the same character repeated.
# - Medium: length is at least 8 and has uppercase/lowercase letters
#   mixed together, or contains digits.
# - Strong: length is at least 8 and contains uppercase letters,
#   lowercase letters, digits, and symbols.
#
# Inputs:
# - password_input (string): The password to evaluate.
#
# Outputs:
# - "Password strength: weak"
# - "Password strength: medium"
# - "Password strength: strong"
#
# Validations:
# - The password cannot be empty.
# - Password length is checked with len().
# ==============================================================================
# Test cases:
# ==============================================================================
# 1) Normal: "Robot123!" -> strong
# 2) Border: "abc" -> weak
# 3) Error: "" -> Error: Invalid input
# ==============================================================================


# Ask the user to enter a password.
password_input = input("Enter a password: ")

# Check if the password is empty.
if len(password_input) == 0:
    # Display an error message if the password is empty.
    print("Error: Invalid input")
else:
    # Initialize a flag to check for uppercase letters.
    has_upper = False

    # Initialize a flag to check for lowercase letters.
    has_lower = False

    # Initialize a flag to check for digits.
    has_digit = False

    # Initialize a flag to check for symbols.
    has_symbol = False

    # Go through each character in the password.
    for character in password_input:
        # Check if the current character is an uppercase letter.
        if character.isupper():
            # Set the uppercase flag to True.
            has_upper = True

        # Check if the current character is a lowercase letter.
        if character.islower():
            # Set the lowercase flag to True.
            has_lower = True

        # Check if the current character is a digit.
        if character.isdigit():
            # Set the digit flag to True.
            has_digit = True

        # Check if the character is neither a letter, a digit, nor a space.
        if not character.isalnum() and not character.isspace():
            # Set the symbol flag to True.
            has_symbol = True

    # Check if the password has fewer than eight characters.
    if len(password_input) < 8:
        # Classify the password as weak.
        print("Password strength: weak")

    # Check if the password contains only lowercase letters.
    elif password_input.isalpha() and password_input.islower():
        # Classify the password as weak.
        print("Password strength: weak")

    # Check if all characters in the password are identical.
    elif len(set(password_input)) == 1:
        # Classify the password as weak.
        print("Password strength: weak")

    # Check if the password contains uppercase letters, lowercase letters, digits, and symbols.
    elif has_upper and has_lower and has_digit and has_symbol:
        # Classify the password as strong.
        print("Password strength: strong")

    # Check if the password contains uppercase and lowercase letters, or at least one digit.
    elif has_upper and has_lower or has_digit:
        # Classify the password as medium.
        print("Password strength: medium")

    else:
        # Classify the password as weak if none of the previous conditions are met.
        print("Password strength: weak")


# ==============================================================================
# Problem 6: Product label formatter
# ==============================================================================
# Description:
# Creates a product label with exactly 30 characters.
#
# Inputs:
# - product_name (string)
# - price_value (string or number)
#
# Outputs:
# - "Label: <exactly 30 characters>"
#
# Validations:
# - Product name cannot be empty after strip().
# - Price must be a positive number.
# ==============================================================================
# Test cases:
# ==============================================================================
# 1) Normal: "Milk", "25.50"
# 2) Border: "A", "1"
# 3) Error: "Milk", "-5"
# ==============================================================================


# Ask the user to enter a product name and remove spaces at the beginning and end.
product_name = input("Enter product name: ").strip()

# Ask the user to enter a product price and remove spaces at the beginning and end.
price_value = input("Enter product price: ").strip()

# Check if the product name is empty.
if product_name == "":
    # Display an error message if the product name is empty.
    print("Error: Invalid product name")
else:
    # Start a block to handle possible errors when converting the price.
    try:
        # Convert the price from a string to a floating-point number.
        price_number = float(price_value)

        # Check if the price is zero or negative.
        if price_number <= 0:
            # Display an error message if the price is not positive.
            print("Error: Invalid price")
        else:
            # Create the product label using the name and price with two decimal places.
            label = f"Product: {product_name} | Price: ${price_number:.2f}"

            # Keep only the first 30 characters of the label.
            label = label[:30]

            # Add spaces at the end if the label has fewer than 30 characters.
            label = label.ljust(30)

            # Display the label between quotation marks to make trailing spaces easier to see.
            print('Label: "' + label + '"')

    # Handle the error if the price cannot be converted to a number.
    except ValueError:
        # Display an error message when the price is invalid.
        print("Error: Invalid price")




# ==============================================================================
# Conclusions:
# ==============================================================================
# String handling is essential for receiving, processing, and displaying data correctly.
# Methods like lower(), strip(), split(), and join() help us clean and organize text.
# Normalizing text before comparing it avoids errors caused by uppercase letters or extra spaces.
# Validations help prevent invalid inputs and unwanted data from causing problems.
# I learned that strings are immutable, so methods return a new string instead of changing the original.
# Slices allow us to extract or reverse parts of a string, depending on what we need.
# ==============================================================================



# ==============================================================================
# References:
# ==============================================================================
# 1) Python Software Foundation. Python Documentation - Text Sequence Type (str).
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
#
# 2) Python Software Foundation. Python Documentation - String Methods.
#    https://docs.python.org/3/library/stdtypes.html#string-methods
#
# 3) Python Software Foundation. Python Tutorial - An Informal Introduction to Python.
#    https://docs.python.org/3/tutorial/introduction.html
#
# 4) W3Schools. Python Strings.
#    https://www.w3schools.com/python/python_strings.asp
#
# 5) W3Schools. Python User Input and Validation.
#    https://www.w3schools.com/python/python_user_input.asp
# ==============================================================================
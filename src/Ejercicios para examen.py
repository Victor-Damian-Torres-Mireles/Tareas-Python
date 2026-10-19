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




# ============================================================
# EXECUTIVE SUMMARY
# ============================================================
# A list is an ordered and mutable collection that can store multiple items.
# A tuple is an ordered and immutable collection whose elements cannot be changed.
# A dictionary stores information as key-value pairs for efficient access by key.
# Lists are useful for product catalogs because items can be added or removed.
# Tuples are useful for fixed data such as coordinates, dates, and configurations.
# Dictionaries are useful for storing records such as names, prices, and identification codes.
# This document presents six problems involving lists, tuples, and dictionaries.
# Each problem includes inputs, outputs, validations, and three test cases.
# The solutions demonstrate searching, inserting, removing, updating, and processing data.
# Input validation and clear output messages help make the programs reliable.
# ============================================================




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




# ============================================================
# Problem 1: Shopping list basics
# ============================================================
# Description:
# This program creates a list of products from user input.
# It adds a new product, counts the total items, and checks
# whether a specific product exists in the list.
#
# Inputs:
# - initial_items_text: Initial products separated by commas.
# - new_item: Product to add to the list.
# - search_item: Product to search for.
#
# Outputs:
# - Items list: Updated list of products.
# - Total items: Number of products in the list.
# - Found item: Boolean indicating whether the product exists.
#
# Validations:
# - The initial input cannot be empty.
# - Empty product names are ignored.
# - The new product and search product cannot be empty.
# ============================================================
# Test cases:
# ============================================================
# 1) Normal: Enter apple, banana, orange; add grape and
#    search for banana. Expected: 4 items, Found item: true.
# 2) Border: Enter apple; add banana and search for pear.
#    Expected: 2 items, Found item: false.
# 3) Error: Enter only spaces as the initial input.
#    Expected: Error: invalid input.
# ============================================================

# Ask for the initial products
initial_items_text = input("Enter products separated by commas: ")

# Validate the initial input
if initial_items_text.strip() == "":
    print("Error: invalid input")
else:
    # Split the text into a list
    items_list = initial_items_text.split(",")

    # Create a new list without empty product names
    clean_items = []

    # Check each product
    for item in items_list:
        item = item.strip()

        if item != "":
            clean_items.append(item)

    # Check that the list contains at least one product
    if len(clean_items) == 0:
        print("Error: invalid input")
    else:
        # Ask for the product to add
        new_item = input("Enter a new product: ").strip()

        # Ask for the product to search for
        search_item = input("Enter a product to search for: ").strip()

        # Validate the product names
        if new_item == "" or search_item == "":
            print("Error: invalid input")
        else:
            # Add the new product
            clean_items.append(new_item)

            # Count the products
            len_list = len(clean_items)

            # Search for the product
            is_in_list = search_item in clean_items

            # Display the results
            print("Items list:", clean_items)
            print("Total items:", len_list)
            print("Found item:", str(is_in_list).lower())







# ============================================================
# Problem 2: Points and distances with tuples
# ============================================================
# Description:
# This program creates two tuples representing points in a
# two-dimensional plane. It calculates the distance between
# the points and creates a tuple with their midpoint.
#
# Inputs:
# - x1, y1: Coordinates of the first point.
# - x2, y2: Coordinates of the second point.
#
# Outputs:
# - Point A: Coordinates of the first point.
# - Point B: Coordinates of the second point.
# - Distance: Distance between both points.
# - Midpoint: Coordinates of the midpoint.
#
# Validations:
# - All four inputs must be numbers.
# - If an input is invalid, display an error message.
# ============================================================
# Test cases:
# ============================================================
# 1) Normal: Point A = (1, 2), Point B = (4, 6).
#    Expected: Distance = 5.0, Midpoint = (2.5, 4.0).
# 2) Border: Both points are (0, 0).
#    Expected: Distance = 0.0, Midpoint = (0.0, 0.0).
# 3) Error: One coordinate contains non-numeric text.
#    Expected: Error: invalid input.
# ============================================================

# Read the coordinates
try:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    # Create the point tuples
    point_a = (x1, y1)
    point_b = (x2, y2)

    # Calculate the distance between the points
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    # Calculate the midpoint
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    # Display the results
    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", round(distance, 2))
    print("Midpoint:", midpoint)

except ValueError:
    # Display an error if an input is not a number
    print("Error: invalid input")





# ============================================================
# 8. CONCLUSIONS
# ============================================================
# Lists are useful for storing and modifying collections of data.
# They allow us to add, search for, and delete elements.
# Tuples are useful for storing data that should not change.
# Dictionaries organize information using keys and values.
# Lists can be combined to relate information by position.
# For example, two lists can store student names and grades.
# Choosing the correct structure makes programs easier to read
# and helps organize information more efficiently.
# ============================================================


# ============================================================
# 9. REFERENCES
# ============================================================
# 1) Python Software Foundation. Built-in Types.
#    https://docs.python.org/3/library/stdtypes.html
#
# 2) Python Software Foundation. Data Structures.
#    https://docs.python.org/3/tutorial/datastructures.html
#
# 3) Python Software Foundation. An Informal Introduction
#    to Python.
#    https://docs.python.org/3/tutorial/introduction.html
#
# 4) Python Software Foundation. Errors and Exceptions.
#    https://docs.python.org/3/tutorial/errors.html
#
# 5) Python Software Foundation. More Control Flow Tools.
#    https://docs.python.org/3/tutorial/controlflow.html
# ============================================================





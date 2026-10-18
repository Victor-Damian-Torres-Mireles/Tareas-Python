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
# 4. EXECUTIVE SUMMARY
# ==============================================================================
# Python provides the int type to store whole numbers and the float type to store numbers with decimal places.
# Integers are useful for counting objects, while floats are used for measurements and calculations involving decimals.
# Boolean values, True and False, represent logical conditions and are commonly produced by comparisons.
# Relational operators compare values, while logical operators combine or modify conditions.
# Type conversion allows data to be transformed using functions such as int(), float(), and bool().
# Validating input data helps prevent incorrect values and ensures that calculations are performed safely.
# Checking value ranges and avoiding division by zero are essential for preventing errors during program execution.
# This document presents six problems involving arithmetic operations, comparisons, logical expressions, and decision-making.
# Each problem includes a description, inputs, outputs, validations, and three test cases: normal, boundary, and error.
# The solutions demonstrate how numeric types and Boolean values can be used to process data and make decisions in Python.
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



# ============================================================
# PROBLEM 1: Temperature Converter and Range Flag
# ============================================================
#
# Description:
# This program converts a temperature from Celsius to Fahrenheit
# and Kelvin. It also determines whether the temperature is high
# based on a threshold of 30.0 degrees Celsius.
#
# Inputs:
# - temp_c (float): Temperature in degrees Celsius.
#
# Outputs:
# - Fahrenheit: Temperature converted to Fahrenheit.
# - Kelvin: Temperature converted to Kelvin.
# - High temperature: true if temp_c >= 30.0, false otherwise.
#
# Validations:
# - Verify that the input can be converted to a float.
# - Reject temperatures below absolute zero (-273.15 Celsius).
# - Ensure that the Kelvin temperature is not below 0.0.
## ============================================================
# Test cases:
# ============================================================
# 1) Normal: Input: 35.0 -> Fahrenheit: 95.0, Kelvin: 308.15,
#    High temperature: true
# 2) Border: Input: 30.0 -> Fahrenheit: 86.0, Kelvin: 303.15,
#    High temperature: true
# 3) Error: Input: "hello" -> Error: invalid input
#
# ============================================================
# PYTHON CODE
# ============================================================

try:  # Start a block to handle invalid numeric input.
    temp_c = float(input("Enter temperature in Celsius: "))  # Read the input and convert it to a floating-point number.

    temp_k = temp_c + 273.15  # Convert the Celsius temperature to Kelvin.

    if temp_k < 0.0:  # Check whether the Kelvin temperature is below absolute zero.
        print("Error: invalid temperature")  # Display an error message if the temperature is physically impossible.
    else:  # Continue if the temperature is valid.
        temp_f = temp_c * 9 / 5 + 32  # Convert the Celsius temperature to Fahrenheit.
        is_high_temperature = temp_c >= 30.0  # Set the Boolean value to True if the temperature is at least 30 degrees Celsius.

        print("Fahrenheit:", round(temp_f, 2))  # Display the Fahrenheit temperature rounded to two decimal places.
        print("Kelvin:", round(temp_k, 2))  # Display the Kelvin temperature rounded to two decimal places.
        print("High temperature:", str(is_high_temperature).lower())  # Display the Boolean result as lowercase true or false.

except ValueError:  # Handle the error if the input cannot be converted to a float.
    print("Error: invalid input")  # Display an error message when the input is not numeric.




# ============================================================
# PROBLEM 2: Work Hours and Overtime Payment
# ============================================================
#
# Description:
# This program calculates a worker's total weekly payment.
# Regular hours are paid at the normal hourly rate, while hours
# exceeding 40 are paid at 150% of the normal hourly rate.
# It also determines whether the worker has overtime hours.
#
# Inputs:
# - hours_worked (float): Total hours worked during the week.
# - hourly_rate (float): Payment per hour.
#
# Outputs:
# - Regular pay: Payment for regular working hours.
# - Overtime pay: Payment for overtime hours.
# - Total pay: Sum of regular and overtime payments.
# - Has overtime: true if hours_worked > 40, false otherwise.
#
# Validations:
# - Verify that both inputs can be converted to floats.
# - Ensure that hours_worked is greater than or equal to 0.
# - Ensure that hourly_rate is greater than 0.
# - Display an error message if an input is invalid.
# ============================================================
# Test cases:
# ============================================================
# 1) Normal: Input: 35 hours, rate 100 -> Regular pay: 3500.00,
#    Overtime pay: 0.00, Total pay: 3500.00, Has overtime: false
# 2) Border: Input: 40 hours, rate 100 -> Regular pay: 4000.00,
#    Overtime pay: 0.00, Total pay: 4000.00, Has overtime: false
# 3) Error: Input: -5 hours, rate 100 ->
#    Error: invalid input
#
# ============================================================
# PYTHON CODE
# ============================================================

try:  # Start a block to handle invalid numeric input.
    hours_worked = float(input("Enter hours worked: "))  # Read the hours worked and convert the value to a float.
    hourly_rate = float(input("Enter hourly rate: "))  # Read the hourly payment and convert the value to a float.

    if hours_worked < 0 or hourly_rate <= 0:  # Check whether the hours or hourly rate are outside the allowed ranges.
        print("Error: invalid input")  # Display an error message if either value is invalid.
    else:  # Continue with the calculations if both inputs are valid.
        regular_hours = min(hours_worked, 40)  # Calculate regular hours, using a maximum of 40 hours.
        overtime_hours = max(hours_worked - 40, 0)  # Calculate overtime hours, ensuring the result is not negative.

        regular_pay = regular_hours * hourly_rate  # Calculate payment for regular working hours.
        overtime_pay = overtime_hours * hourly_rate * 1.5  # Calculate overtime payment at 150% of the normal rate.
        total_pay = regular_pay + overtime_pay  # Add regular and overtime payments to obtain the total pay.

        has_overtime = hours_worked > 40  # Set the Boolean value to True if the worker exceeded 40 hours.

        print("Regular pay:", round(regular_pay, 2))  # Display regular payment rounded to two decimal places.
        print("Overtime pay:", round(overtime_pay, 2))  # Display overtime payment rounded to two decimal places.
        print("Total pay:", round(total_pay, 2))  # Display total payment rounded to two decimal places.
        print("Has overtime:", str(has_overtime).lower())  # Display the Boolean result as lowercase true or false.

except ValueError:  # Handle inputs that cannot be converted to floating-point numbers.
    print("Error: invalid input")  # Display an error message when an input is not numeric.




# ============================================================
# PROBLEM 3: Discount Eligibility with Booleans
# ============================================================
#
# Description:
# This program determines whether a customer qualifies for a discount.
# A customer is eligible if they are a student, a senior, or their
# purchase total is at least 1000.0.
# Eligible customers receive a 10% discount on their purchase.
#
# Inputs:
# - purchase_total (float): Total purchase amount.
# - is_student_text (string): "YES" or "NO" indicating student status.
# - is_senior_text (string): "YES" or "NO" indicating senior status.
#
# Outputs:
# - Discount eligible: true if the customer qualifies, false otherwise.
# - Final total: Purchase amount after applying any eligible discount.
#
# Validations:
# - Verify that purchase_total can be converted to a float.
# - Ensure that purchase_total is greater than or equal to 0.0.
# - Normalize student and senior responses to uppercase.
# - Accept only "YES" or "NO" for both status inputs.
# - Display an error message if any input is invalid.
# ============================================================
# Test cases:
# ============================================================
# 1) Normal: Input: 500.0, YES, NO -> Discount eligible: true,
#    Final total: 450.0
# 2) Border: Input: 1000.0, NO, NO -> Discount eligible: true,
#    Final total: 900.0
# 3) Error: Input: -50.0, YES, NO ->
#    Error: invalid input
#
# ============================================================
# PYTHON CODE
# ============================================================

try:  # Start a block to handle invalid numeric input.
    purchase_total = float(input("Enter purchase total: "))  # Read the purchase amount and convert it to a float.
    is_student_text = input("Is the customer a student? (YES/NO): ").strip().upper()  # Read the student response, remove extra spaces, and convert it to uppercase.
    is_senior_text = input("Is the customer a senior? (YES/NO): ").strip().upper()  # Read the senior response, remove extra spaces, and convert it to uppercase.

    if purchase_total < 0 or is_student_text not in ("YES", "NO") or is_senior_text not in ("YES", "NO"):  # Check whether the purchase amount or either response is invalid.
        print("Error: invalid input")  # Display an error message if any input is invalid.
    else:  # Continue if all inputs pass validation.
        is_student = is_student_text == "YES"  # Convert the student response into a Boolean value.
        is_senior = is_senior_text == "YES"  # Convert the senior response into a Boolean value.

        discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)  # Determine eligibility if any of the three conditions is true.

        if discount_eligible:  # Check whether the customer qualifies for the discount.
            final_total = purchase_total * 0.9  # Apply a 10% discount to the purchase total.
        else:  # Execute this block if the customer does not qualify for a discount.
            final_total = purchase_total  # Keep the original purchase total without a discount.

        print("Discount eligible:", str(discount_eligible).lower())  # Display the eligibility result as lowercase true or false.
        print("Final total:", round(final_total, 2))  # Display the final amount rounded to two decimal places.

except ValueError:  # Handle a purchase amount that cannot be converted to a float.
    print("Error: invalid input")  # Display an error message when the numeric input is invalid.





# ============================================================
# PROBLEM 4: Basic Statistics of Three Integers
# ============================================================
#
# Description:
# This program reads three integers and calculates their sum,
# average, maximum, and minimum values.
# It also determines whether all three integers are even.
#
# Inputs:
# - n1 (int): First integer.
# - n2 (int): Second integer.
# - n3 (int): Third integer.
#
# Outputs:
# - Sum: Sum of the three integers.
# - Average: Arithmetic mean of the three integers.
# - Max: Maximum value among the three integers.
# - Min: Minimum value among the three integers.
# - All even: true if all three integers are even, false otherwise.
#
# Validations:
# - Verify that all three inputs can be converted to integers.
# - Allow positive numbers, negative numbers, and zero.
# - Display an error message if any input is not an integer.
## ============================================================
# Test cases:
# ============================================================
# 1) Normal: Input: 4, 6, 8 -> Sum: 18, Average: 6.0,
#    Max: 8, Min: 4, All even: true
# 2) Border: Input: 0, -2, 2 -> Sum: 0, Average: 0.0,
#    Max: 2, Min: -2, All even: true
# 3) Error: Input: 4, "hello", 8 ->
#    Error: invalid input
#
# ============================================================
# PYTHON CODE
# ============================================================

try:  # Start a block to handle inputs that are not valid integers.
    n1 = int(input("Enter the first integer: "))  # Read the first input and convert it to an integer.
    n2 = int(input("Enter the second integer: "))  # Read the second input and convert it to an integer.
    n3 = int(input("Enter the third integer: "))  # Read the third input and convert it to an integer.

    sum_value = n1 + n2 + n3  # Calculate the sum of the three integers.
    average_value = sum_value / 3  # Calculate the arithmetic mean as a floating-point number.
    max_value = max(n1, n2, n3)  # Find the largest of the three integers.
    min_value = min(n1, n2, n3)  # Find the smallest of the three integers.

    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)  # Check whether all three integers are divisible by two.

    print("Sum:", sum_value)  # Display the sum of the three integers.
    print("Average:", round(average_value, 2))  # Display the average rounded to two decimal places.
    print("Max:", max_value)  # Display the maximum value.
    print("Min:", min_value)  # Display the minimum value.
    print("All even:", str(all_even).lower())  # Display the Boolean result as lowercase true or false.

except ValueError:  # Handle an input that cannot be converted to an integer.
    print("Error: invalid input")  # Display an error message if any input is invalid.





# ============================================================
# PROBLEM 5: Loan Eligibility (Income and Debt Ratio)
# ============================================================
#
# Description:
# This program determines whether a person qualifies for a loan
# based on their monthly income, monthly debt, and credit score.
# It calculates the debt ratio and evaluates the eligibility rules.
#
# Inputs:
# - monthly_income (float): Person's monthly income.
# - monthly_debt (float): Person's monthly debt payments.
# - credit_score (int): Person's credit score.
#
# Outputs:
# - Debt ratio: Monthly debt divided by monthly income.
# - Eligible: true if all loan requirements are met, false otherwise.
#
# Validations:
# - Verify that income and debt can be converted to floats.
# - Verify that the credit score can be converted to an integer.
# - Ensure that monthly_income is greater than 0.0.
# - Ensure that monthly_debt and credit_score are not negative.
# - Display an error message if any input is invalid.
# ============================================================
# Test cases:
# ============================================================
# 1) Normal: Input: income 10000.0, debt 3000.0, score 700 ->
#    Debt ratio: 0.3, Eligible: true
# 2) Border: Input: income 8000.0, debt 3200.0, score 650 ->
#    Debt ratio: 0.4, Eligible: true
# 3) Error: Input: income 0.0, debt 1000.0, score 700 ->
#    Error: invalid input
#
# ============================================================
# PYTHON CODE
# ============================================================

try:  # Start a block to handle inputs that cannot be converted to the required numeric types.
    monthly_income = float(input("Enter monthly income: "))  # Read the monthly income and convert it to a float.
    monthly_debt = float(input("Enter monthly debt: "))  # Read the monthly debt payments and convert them to a float.
    credit_score = int(input("Enter credit score: "))  # Read the credit score and convert it to an integer.

    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:  # Check whether any input is outside the allowed range.
        print("Error: invalid input")  # Display an error message if any input is invalid.
    else:  # Continue if all inputs pass validation.
        debt_ratio = monthly_debt / monthly_income  # Calculate the proportion of monthly income used to pay debt.
        eligible = monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650  # Check whether all loan eligibility requirements are satisfied.

        print("Debt ratio:", round(debt_ratio, 2))  # Display the debt ratio rounded to two decimal places.
        print("Eligible:", str(eligible).lower())  # Display the eligibility result as lowercase true or false.

except ValueError:  # Handle inputs that cannot be converted to the required numeric types.
    print("Error: invalid input")  # Display an error message if any input is not numeric in the required format.





# ============================================================
# PROBLEM 6: Body Mass Index (BMI) and Category Flag
# ============================================================
#
# Description:
# This program calculates a person's Body Mass Index (BMI)
# using their weight in kilograms and height in meters.
# It classifies the BMI as underweight, normal, or overweight
# using Boolean values and the specified BMI ranges.
#
# Inputs:
# - weight_kg (float): Person's weight in kilograms.
# - height_m (float): Person's height in meters.
#
# Outputs:
# - BMI: Calculated BMI rounded to two decimal places.
# - Underweight: true if BMI is below 18.5, false otherwise.
# - Normal: true if BMI is between 18.5 and 25.0, false otherwise.
# - Overweight: true if BMI is 25.0 or higher, false otherwise.
#
# Validations:
# - Verify that both inputs can be converted to floats.
# - Ensure that weight_kg is greater than 0.0.
# - Ensure that height_m is greater than 0.0.
# - Display an error message if any input is invalid.
# ============================================================
# Test cases:
# ============================================================
# 1) Normal: Input: weight 70.0, height 1.75 ->
#    BMI: 22.86, Underweight: false, Normal: true,
#    Overweight: false
# 2) Border: Input: weight 80.0, height 1.60 ->
#    BMI: 31.25, Underweight: false, Normal: false,
#    Overweight: true
# 3) Error: Input: weight -5.0, height 1.70 ->
#    Error: invalid input
#
# ============================================================
# PYTHON CODE
# ============================================================

try:  # Start a block to handle inputs that cannot be converted to floats.
    weight_kg = float(input("Enter weight in kilograms: "))  # Read the person's weight and convert it to a float.
    height_m = float(input("Enter height in meters: "))  # Read the person's height and convert it to a float.

    if weight_kg <= 0 or height_m <= 0:  # Check whether the weight or height is zero or negative.
        print("Error: invalid input")  # Display an error message if either measurement is invalid.
    else:  # Continue if both measurements are greater than zero.
        bmi = weight_kg / (height_m * height_m)  # Calculate BMI by dividing weight by height squared.

        is_underweight = bmi < 18.5  # Check whether the BMI is below 18.5.
        is_normal = 18.5 <= bmi < 25.0  # Check whether the BMI is at least 18.5 and below 25.0.
        is_overweight = bmi >= 25.0  # Check whether the BMI is 25.0 or higher.

        print("BMI:", round(bmi, 2))  # Display the BMI rounded to two decimal places.
        print("Underweight:", str(is_underweight).lower())  # Display the underweight result as lowercase true or false.
        print("Normal:", str(is_normal).lower())  # Display the normal-weight result as lowercase true or false.
        print("Overweight:", str(is_overweight).lower())  # Display the overweight result as lowercase true or false.

except ValueError:  # Handle inputs that cannot be converted to floating-point numbers.
    print("Error: invalid input")  # Display an error message if either input is invalid.




# ============================================================
# CONCLUSIONS
# ============================================================
# Integers and floats work together to perform calculations with whole numbers and decimal values.
# Comparisons produce Boolean values that allow programs to make decisions using if statements.
# Validating input ranges helps prevent incorrect data and unexpected results.
# Avoiding division by zero is essential to prevent runtime errors during calculations.
# I learned how to combine conditions using and, or, and not to evaluate multiple requirements.
# These programming techniques are useful for calculating salaries, discounts, loan eligibility, and BMI.
# Using appropriate data types and clear validations makes programs more reliable and easier to understand.
# ============================================================





# ============================================================
# REFERENCES
# ============================================================
#
# 1) Python Software Foundation. Built-in Types - Numeric Types.
#    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
#
# 2) Python Software Foundation. Built-in Types - Boolean Type.
#    https://docs.python.org/3/library/stdtypes.html#boolean-type-bool
#
# 3) Python Software Foundation. Expressions - Operators and Comparisons.
#    https://docs.python.org/3/reference/expressions.html#operator-precedence
#
# 4) Python Software Foundation. Built-in Functions - int(), float(), and bool().
#    https://docs.python.org/3/library/functions.html
#
# 5) Python Software Foundation. Python Tutorial - More Control Flow Tools.
#    https://docs.python.org/3/tutorial/controlflow.html
#
# ============================================================

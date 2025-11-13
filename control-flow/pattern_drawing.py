# pattern_drawing.py
# Draw a square pattern of asterisks using nested loops

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop for rows
while row < size:
    # Inner loop for columns
    for col in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Move to next row
    row += 1

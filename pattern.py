n = int(input("Enter the number of rows: "))

for i in range(n):
    # Print leading spaces
    for j in range(n - i - 1):
        print(" ", end="")
    
    # Print stars
    for k in range(2 * i + 1):
        print("*", end="")
    
    # Move to next line
    print()
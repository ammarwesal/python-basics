# Input format: [1,2,3],[4,5,6],[7,8,9]
input_str = input("Enter nested list (format: [1,2,3],[4,5,6]): ")
z = [list(map(str, sublist.strip('[]').split(','))) for sublist in input_str.split('],[')]
print("Nested list:", z)

# Flatten it
new = [x for sublist in z for x in sublist]
print("Flattened list:", new)
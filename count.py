# List of first names
names =list(input("enter the names: ").split())

# Count occurrences of 'a' (case-insensitive)
count = sum(name.lower().count('a') for name in names)

print("Total occurrences of 'a':", count)

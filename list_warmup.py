# Create a list containing four fruits
fruits = ["Pineapple", "banana", "Guava", "mango"]

# Print the first and the last item using indexes
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# .append() a fifth fruit, then print the whole list
fruits.append("orange")
print("After append:", fruits)

# .remove() one fruit, then print the list again
fruits.remove("banana")
print("After remove:", fruits)

# Print how many fruits remain using len()
print("Number of fruits remaining:", len(fruits))

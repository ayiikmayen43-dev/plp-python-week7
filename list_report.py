items = ["phone", "avocado", "milk", "sweet potatoes", "sugar"]

# 1. Print each item numbered (1. bread, 2. avocado, ...)
print("Numbered List:")
for index, item in enumerate(items, start=1):
    print(f"{index}. {item}")

# 2. Count how many item names have more than 4 letters
long_name_count = 0
for item in items:
    if len(item) > 4:
        long_name_count += 1

print(f"\nNumber of items with more than 4 letters: {long_name_count}")

# 3. Find and print the longest item name using a loop comparison
longest_item = items[0]
for item in items:
    if len(item) > len(longest_item):
        longest_item = item

print(f"The longest item name is: {longest_item}")

fruits = {"Apple", "Banana", "Cherry", "Apple", "Kiwi"}
basket = frozenset(fruits)

print('Unique elements:', basket)

# Add new fruit throws an error!
basket.add("Orange")

print('After adding new element:', basket)

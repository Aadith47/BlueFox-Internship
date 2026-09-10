fruits = ["apple", "orange", "blueberry"]

def fruit_appending(fruit):
    fruits.append(fruit)
    removed_fruit = fruits.pop(1)
    return removed_fruit

def main():
    fruit = input("Enter a fruit: ")
    removed_fruit = fruit_appending(fruit)
    print(f"Removed fruit={removed_fruit}")
    print(f"Fruits={fruits}")

main()
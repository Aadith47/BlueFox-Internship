def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"

def main():
    print(greet("Sam"))
    print(greet("Sam", greeting="Hi"))

main()
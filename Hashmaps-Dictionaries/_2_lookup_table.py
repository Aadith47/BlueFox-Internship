def key_values_squares():

    squares={}

    for num in range(1, 10):
        squares[num]= num * num
    return squares


def main():

    result1=key_values_squares()
    print(result1)

main()


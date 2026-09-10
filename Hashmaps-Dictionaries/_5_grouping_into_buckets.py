list1=["apple","avacado","cherry","orange"]
grouped = {}
def buckets():

    for word in list1:
        first_letter = word[0]
        if first_letter not in grouped:
            grouped[first_letter] = []
        grouped[first_letter].append(word)

    return grouped

def main():

    result1=buckets()
    print(result1)

main()





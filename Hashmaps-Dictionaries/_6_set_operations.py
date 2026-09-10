list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 6, 7, 8]

duplicate_items = []


def set_operation():

    for i in list1:
        if i in list2:
            duplicate_items.append(i)
    return duplicate_items
def main():

    result1=set_operation()
    print(result1)

main()

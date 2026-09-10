list1 = [1, [2, 3], [4, [5, 6]]]
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def main():

    result1=flatten(list1)
    print(result1)

main()
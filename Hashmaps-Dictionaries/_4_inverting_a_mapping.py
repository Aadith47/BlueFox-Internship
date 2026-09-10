dict1 = {"a": 1, "b": 2}
def invertion():
    
    dict2 = {}
    for key, value in dict1.items():
        dict2[value] = key

    return dict2

def main():

    result1=invertion()
    print(result1)

main()

    
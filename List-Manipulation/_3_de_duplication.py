list_of_number=[1,4,2,8,4,2,6]
list_of_unique=[]
def uniques():

    for i in (list_of_number):
        if i not in list_of_unique:
            list_of_unique.append(i)

    return list_of_unique

def main():

    result1=uniques()
    print(result1)

main()

list1=[1,2,3,4,5]
def func(n):
    
    list2 = list1[n:] + list1[:n]
    return list2

def main():

    n=int(input("Enter the number of rotation: "))
    result1=func(n)
    print(result1)

main()

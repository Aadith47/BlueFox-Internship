list1=[1,2,3,4,5,6,7,8,9,10]
list_even=[]
list_odd=[]

def func():
    for i in (list1):
        if i % 2 == 0:
            list_even.append(i)
        else:
            list_odd.append(i)

def main():
    
    func()
    print(f"Even List = {list_even}\nOdd List = {list_odd}")

main()





# def main():

#     list1=[1,2,3,4,5,6,7,8,9,10]
#     list_even=[]
#     list_odd=[]

#     for i in (list1):
#         if i % 2 == 0:
#             list_even.append(i)
#         else:
#             list_odd.append(i)

#     print(f"Even List = {list_even}\nOdd List = {list_odd}")

# main()

list1=[1,3,4,6,8,12,5,]
list2=[20,21,83,45,67,80,44]

even_list=[]
odd_list=[]

def func():
    for i in list1:

        if i % 2 == 0:
            even_list.append(i)

    for j in list2:

        if j % 2 != 0:
            odd_list.append(j)


def main():

    func()
    print(f"Evens from first list = {even_list}\n Odds from second list = {odd_list}")

main()

        


def sum_of_two(*args):
    return sum(args)

def average_of_two(*args):
    total=sum(args)
    count=len(args)
    return total/count

def main():
    result1 = sum_of_two(10,23,56,78)
    result2 = average_of_two(56,12,34,55)
    print(f"{result1}\n{result2}")
    
main()

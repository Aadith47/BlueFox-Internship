def avg(*args):
    total = sum(args)
    count = len(args)
    return total/count

def main():
    result = avg(4, 8, 15, 16)
    print(result)
    
main()
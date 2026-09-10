def intrest_calc(P,R,T):
    result = (P*R*T)/100
    return result

def main():

    P=int(input("Enter the Principal "))
    R=int(input("Enter the Rate "))
    T=int(input("Enter the time "))

    print(f"{intrest_calc(P,R,T)}")

main()

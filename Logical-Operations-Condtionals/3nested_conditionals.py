#Write a program that classifies a triangle as equilateral, isosceles, or scalene based on its three side lengths. Sample: Input: 5, 5, 5 → Output: Equilateral 
def equilateral(side1,side2,side3):
    result = side1==side2==side3
    return result

def isosceles(side1,side2,side3):
    result = side1==side2 or side1 == side3 or side2 == side3
    return result

def main():

    side1=float(input("Enter First side: "))
    side2=float(input("Enter second side: "))
    side3=float(input("Enter third side: "))

    equilateral1=equilateral(side1,side2,side3)
    isosceles1=isosceles(side1,side2,side3)

    if equilateral1:
        print("Triange is Equilateral")

    elif isosceles1:
        print("Triange is isosceles")

    else:
        print("Scalene")
main()
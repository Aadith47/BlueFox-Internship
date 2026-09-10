def leap_year_calc(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
def main():

    year = int(input("Enter the year: "))
    leap_year = leap_year_calc(year)

    if leap_year:
        print(f"{year} is leap year")

    else:
        print(f"{year} is not a leap year")

main()
# Base price depends on show time — Morning ($5), Afternoon ($8), Evening ($12)
# Age-based rules — kids (under 12) get 50% off, seniors (60+) get 30% off, everyone else pays full price
# Day-based surge pricing — weekends add a $2 surcharge (compound condition: is it Sat/Sun AND evening show?)
# Group discount — if booking 4+ tickets at once, apply an additional 10% off the total
# Final output — print an itemized breakdown: base price, discount applied, surcharge applied, final total

def time_based_rules(choice1):
    if choice1 == "M":
        return 5
    elif choice1 == "A":
        return 8
    else:
        return 12


def age_based_rules(age):
    if age >= 60:
        return 0.30
    elif age <= 12:
        return 0.50
    else:
        return 0


def day_based_rules(choice3):
    if choice3 == "Saturday" or choice3 == "Sunday":
        return 2
    else:
        return 0


def group_based_discount(choice4):
    if choice4 >= 4:
        return 0.10
    else:
        return 0


def main():

    choice1 = input("What show do you prefer Morning:M, Afternoon:A, Evening:E: ")
    age = int(input("Age: "))
    choice3 = input("Day (e.g. Saturday, Sunday, Monday): ")
    choice4 = int(input("Number of persons: "))

    base_price = time_based_rules(choice1)
    age_discount = age_based_rules(age)
    day_surcharge = day_based_rules(choice3)
    group_discount = group_based_discount(choice4)

    price_per_ticket = base_price - (base_price * age_discount)
    price_per_day = price_per_ticket + day_surcharge
    discounted_price = price_per_day - (price_per_day * group_discount)
    total=(discounted_price * choice4)

    print(f"Base Price: ${base_price}")
    print(f"Age discount: {age_discount*100}%")
    print(f"Day surcharge: ${day_surcharge}")
    print(f"Group discount: {group_discount*100}%")
    print(f"Per Head: ${discounted_price}")
    print(f"The total of {choice4} members=${total}")

main()
def length_in_pass(password):
   if len(password) < 8:
      return "MUST CONTAIN 8 CHARACTERS"
   else:
      return ""

def uppercase_in_pass(password):
   if not any(char.isupper() for char in password):
      return "MUST CONTAIN AN UPPERCASE LETTER"
   else:
      return ""

def digit_in_pass(password):
   if not any(char.isdigit() for char in password):
      return "MUST CONTAIN A DIGIT"
   else:
      return ""

def main():

    password=input("Enter the passsword:")

    result1 = length_in_pass(password)
    result2 = uppercase_in_pass(password)
    result3 = digit_in_pass(password)


    if result1 == "" and result2 == "" and result3 == "":
        print("Strong password!")

    else:
        print("Password:")

        if result1:
            print(result1)

        if result2:
            print(result2)

        if result3:
            print(result3)
      

main()
    
      

def capitalizing(string):

      words = string.split()
      result1=""
      for word in words:
            result1 += word[0].upper() + word[1:] + " "
      return result1


def main():

      string = (input("Enter the sentence: "))
      result1=capitalizing(string)
      print(f"{result1}")

main()
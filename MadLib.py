#MadLib.py
#Name: Carter Bowman
#Date: 8/23/24
#Assignment:

def main():
  print("Madlib")
  #Ask user for words
  name1 = input("Enter a name: ")
  place1 = input("Enter a place:  ")
  friend1 = input("Enter a friends name:  ")
  verb1 = input("Enter a action verb: ")
  friend2 = input("enter a friends name: ")
  verb2 = input("enter a action verb: ")
  #Print the story with the user supplied words.
  print("Hello, my name is", name1)
  print("and I live in", place1)
  print("my best friends name is", friend1)
  print("In the summer we like to", verb1 , "with our other friend", friend2, ".C") 
  print("In the winter we like to", verb2)
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()

def welcome_user():
  print("Welcome to _____!")
  print("I'm your friendly chatbot, here to help you.")
    
def get_user_info():
  name = input("What's your name? ")
  age = input("How old are you? ")
  return name, age

def display_menu():
  print("How may I assist you today?")
  print("1. PLaceholder")
  print("2. PlaceHolder")
  print("3. Placeholder")
  print("4. PLaceholder")
  print("5. Exit")
  choice = input("Pick one of the option given, 1-5: ")

def chatbot():
  welcome_user()
  get_user_info()
  display_menu()

import time

#Version 1.0
#Main features - Create account system, log-in verify credentials, create bill list
#total the amount of bills based on input, logout functionality, menu selection

#Create Plan for the budget app
#If the date of bill is before pay date then list upcoming charges
# Week 1  total bills net total for the month and that would
# projected savings

# list_of_bills.append(
#   {"bill_name": "Gas", "date": "08-01-2022", "amount": 20})

# Set this up by parsing a file
# Each file would be it's own month


#--------------------------------------------------------------#
def input_additional_bill():
  while True : 
    Reply = input("Would you like to enter another bill (y/n). ").lower()
    if Reply == "n" or Reply == "no":
      print("You replied with ", Reply)
      time.sleep(1)
      print("You have successfully created your list of bills.")
      time.sleep(1)
      return False
    elif Reply == "y" or Reply == "yes":
      print("You replied with ", Reply)
      return True
    else:
      print("Invalid input entered.")

#--------------------------------------------------------------#
def add_to_list(bill,list_of_bills):
  list_of_bills.append(bill)
  print()
  print("Bills:")
  for bill in list_of_bills:
    print()
    print(type(bill["amount"]))

  print()
  return (list_of_bills)
#--------------------------------------------------------------#
def create_bill(name,date,amount):
  name = input("Enter Bill Name").lower()
  date = str(input("Enter date ex. mm-dd-yyyy"))
  # Add try to catch this error just in case a string is inputted
  amount = int(input("Enter the amount"))
  
  return {"name":name,"date":date,"amount":amount}
  
#--------------------------------------------------------------#
# Budget creator
def create_budget(list_of_bills):
  #Generator Is Active
  Continue_generator =  True
  #Bill Variables
  name = ''
  date = ''
  amount = 0
  
  while Continue_generator:
    bill = create_bill(name,date,amount)
    list_of_bills = add_to_list(bill,list_of_bills)
    Continue_generator = input_additional_bill()
    # print(generate_bill)
  return list_of_bills

  
  
#--------------------------------------------------------------#
#Sum all of the bills
def total_bills(list_of_bills):
  total_bills = 0
  for bill in list_of_bills:
    total_bills += bill["amount"]
  print(total_bills)

#--------------------------------------------------------------#
# Easy Breaking Point
# Important Spot
def Select_menu_option(list_of_bills):
  print()
  print("Here are some hotkeys for you.")
  time.sleep(2)
  print()
  print("- Total Bills/TB")
  time.sleep(1)
  print("- Logout")
  time.sleep(1)
  print()
  
  Reply = input("What would you like to do next.").lower()
  print(Reply)
  if Reply == "total bills" or Reply == "tb":
    total_bills(list_of_bills)
  elif Reply == "logout":
    print("Closing program in")
    for x in range(3,0,-1):
      print(x)
      time.sleep(1)
    quit()
  else:
    print("Invalid input entered:", Reply)
  return True

#--------------------------------------------------------------#

# This is the main function
def show_menus():
  bill_list_generated = ""
  # Total_income = input("Input your total income for the month")
  print()
  #Bill List
  list_of_bills = []
  print("Enter all of your upcoming bills.")
  print()
  list_of_bills = create_budget(list_of_bills)
  
  if len(list_of_bills) >= 1:
    bill_list_generated =  True
    
  if bill_list_generated:
    menu_active = True
    while menu_active:
      menu_active = Select_menu_option(list_of_bills)

#--------------------------------------------------------------#

# This function verifies the user
def Verify_User():
  attempts = 3
  print("Welcome to Budget Buddy!")
  time.sleep(2)
  print("Create an account to access the tool.")
  time.sleep(1)
  #add a conditional to make sure the Username is the proper length
  Username = input("Create a username.\n")
  #add a conditional to make sure the Password is the proper length
  Password = input("Create a password.\n")
  print()
  while attempts > 0: 
    time.sleep(1)
    print("Enter your login information")
    print()
    time.sleep(1)
    UserField = input("Enter Username\n")
    PasswordField = input("Enter Password\n")

    time.sleep(1)
    
    if UserField == Username and PasswordField == Password:
      print("Welcome back ", Username)
      show_menus()
    elif attempts > 1: 
      print()
      print("Incorrect Username and Password Combination. \nTry again.\n")
      attempts -= 1
      print("You have", attempts, "attempts left.\n")
    else: 
      print("You have been locked out")
      attempts -= 1


Verify_User()

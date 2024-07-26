
# So far I have learned how to parse files better and recreate a dictionary using data
# using user inputs to create new files, look up files, Using is functions to find
# file paths and return a list of files using os.listdir(), os.getcwd()
# Functions can be invoked without a reference because they are independent
# Methods require a reference to the class to be used
# Filter through data based on user input
# Iterate over objects to get the exact data that I need
########################
# I want to add ...
# User add bills to existing file 
# make changes to file that is open
#navigate through "app" based on whether a file is open or not 
#Main menu for opening file, creating a file, deleting a file, logging out
# When openening file you can add bill, delete bill, close file
# Need to be able to remove a bill after its opened
#Make calculations based on the file that is open using the show
#Changes made
# Added a number selection system to input number instead of text to reduce error
# When a user selects open file they can confirm that they want to open and are
# shown a list of bills in that file

#Changes made 7/9/24
# Create a new budget, with the ability to name the budget, delete budget
# The user needs to be asked what month it is, view budget for month, week categories 
# create/delete new categories
# have the option to delete and restart the months budget when they open file ask what month it is


# Instead of having multiple files that are directly accessible in the directory I put everything in a specific folder, each folder is it's on budget. 
# There are fewer functions which will improve the readability of the program
# The whole point before was to have separate text files that were monthly budgets but I didnt consider
# different categories were necessary too, so not having folders for each month was going to be confusing
#also each "bill" before was an object that listed the category, date, amount, but every single budget item was in one big file instead of it being separated and organized . This new way streamlines the process and puts things in viewable categories that the user can then download or export

import time
import os
import calendar 




# file = open("Texttfile.txt","w")
# bills = ["hello","There","my","love"]
# for word in bills:
  
#   file.write(f"{word}\n")
# file.close()

# file = open("Texttfile.txt","r")
# for line in file:
#   print(line.strip())





# Testing how the find method is used

# file = "string.txt"

# x = file.find("s")
# print(file[x])
#------------------------------------


#------------------------------------------------------------
def welcome_user():

  not_ready = True
  
  while not_ready:
    # User inputs the number to the corresponding text file
    print("Welcome to Budget Buddy!")
    Reply = input("Are you ready to get started?\n").lower()
    if Reply == "yes" or Reply == "y":
      not_ready = False
      
    
  

#-----------------------------------------------------------
def create_list_of_bills(list_of_bills,file,FileName):
  good_format = False
  for line in file:
    # Splits line into a list
    data = line.strip().split(",")
    # Can change based on the main format of the file, currently three keys in dict
    if(len(data) == 3):
      
      good_format = True
      list_of_bills.append({'name':data[0],'date':data[1],'amount':data[2]})
  print("You are working in ", FileName)
  
  # Take this out because its never going to happen
  if not good_format: 
      print("Invalid data format.")
      # open_file_menu()
  return list_of_bills

#----------------------------------------------#
# These functions will control what is done to the open file

def add_bill(FileName):
  
  is_active = True
  while is_active:
    file = open(FileName, "a")
    Name_of_Bill = input("Enter the name of Bill")
    Date_of_Bill = str(input("Enter the date of Bill"))
    # Check to see if this has to be a number when written to the file
    Amount_of_Bill = input("Enter the amount of Bill")

    file.write(f"{Name_of_Bill},{Date_of_Bill},{Amount_of_Bill}\n")
    file.close()
    #put this in loop
    print("Would you like to add another bill?")
    Reply = input("Confirm (y/n)").lower()
    if Reply == "yes" or Reply == "y":
      continue
    elif Reply == "no" or Reply == "n":
      is_active = False
    
      
def get_month_input():
  no_input = True
  month_dict = {
    "january": 1,
    "february": 2,
    "march" : 3,
    "april" : 4,
    "may" : 5,
    "june" : 6,
    "july" : 7,
    "august" : 8,
    "september" : 9,
    "october" : 10,
    "november" : 11,
    "december" : 12
  }
  while no_input:
    month = input("What is the current month?").lower()
    for month_key in month_dict:
      if month_key == month:
        return month_key
    print("Please enter a valid month.")


def find_month(month):
  
  month_dict = {
    "january": 1,
    "february": 2,
    "march" : 3,
    "april" : 4,
    "may" : 5,
    "june" : 6,
    "july" : 7,
    "august" : 8,
    "september" : 9,
    "october" : 10,
    "november" : 11,
    "december" : 12
  }
  
  for str in month_dict:
    if str == month :
      return month_dict[str]


def create_category():
  folder_path = "Budget" 
  #Create additional categories if necessary
  while True:
    # Make sure the category name is lowercased
    category_name = input("Name your category").lower()
  
    file_path = os.path.join(folder_path,f"{category_name}")
    
    file = open(f"{file_path}.txt","w")
    print("hello")
    #Confirm if they want to continue loop
    while True:
      response = input("Would you like to add another category?").lower()
      if response == "no" or response == "n":
        return
      elif response == "yes" or response == "y":
        break
      print("Enter a valid command")

def delete_category():
  #create a view of the files to edit that don't have the txt extension str
  # Make sure the category is always lower cased
  # Food
  # Utilities
  while True:
    category = input("Select a category to remove.").lower()
    confirming = ""

    folder_path = "Budget"

    file_path = os.path.join(folder_path,f"{category}.txt")

    if os.path.exists(file_path):
      while True:
        response = input("Are you sure you want to delete this").lower()
        if response == "yes" or response == "y":
          os.remove(file_path)
          confirming = True
          break
        elif response == "no" or response == "n":
          break
        else:
          print("Please enter yes or no.")
    else:
      print("This category does not exist.")

    while confirming:
      reply = input("Would you like to remove another category").lower()
      if reply == "yes" or reply == "y":
        break
      if reply == "no" or reply == "n":
        return
      print("Please enter yes or no.")
      
#------------------------------------------------------#
# This is the main loop for the program, this handles all the commands
def list_commands():
  while True:
    print("This menu is to manage your categories.")
    print("Select an option from the menu.")
    print("")
    # The stuff that modifies the categories should have a serparate menu 
    print("create or c")
    print("delete or d")
    # This should have its own separate menu of things to do like adding and removing a bill
    # This should be able to add a transaction to the category of choice
    # remove a transaction can list 1 - however many things there are in the category and it will remove whatever user selects 
    print("add a transaction")
    
    print("list ")
    # Get the users input by selecting a command  
    command = input("Select an option \n").lower()
  
    if command == "create" or command == "c":
      create_category()

    if command == "delete" or command == "d":
      delete_category()
    # Need to add a print statement that says enter a proper command/command invalid 7/10/24
    # if command == "modify" or command == "m":
    #   modify_category()
#----------------------------------------------#
def start_app():
  list_of_bills = []
  curr_file_list = []
  file_dict = []
  # This welcomes the user
  welcome_user()


  # Add a function to check whether the input is an actual month 7/9/24
  # create one variable that lists the month_dictionary 
  month = get_month_input()
  
  year = int(input("What is the current year?"))

  print("")
  
  month_int = find_month(month)
  # Use this calendar printout for later 7/9/24
  calendar.prmonth(year,month_int)
  print("")
  
  list_commands()
  

  
  

  print("")


# calendar.prmonth(year,name)

# try:
  #   #This needs to be put in a helper function 
  #   file = open(FileName,"r")

    
    
  #   list_of_bills = create_list_of_bills(list_of_bills,file,FileName)
  #   file.close()
  #   #-------------------------------------------------------------------
  #   #Change the order of what is happening here 7/9/24

  #   if list_of_bills != []:

  #     # def month = 
  #     # calendar.prmonth(2024,month)
  #     print("Bills:")

  #   for line in list_of_bills:
  #     print(line)
  #   #-----------------------------------------#
  #   # Menu when the file is open
  #   print("Select an option from below.")
  #   print("- Add Bill")
  #   Reply = input("What would you like to do?").lower()
  #   if Reply == "add bill":
  #     add_bill(FileName)
  #   else:
  #     print("incorrect command input.")
  #   # Print each bill from list_of_bills

  #   print("Will that be the end of today's session?")
      
  # except FileNotFoundError:
  #   # Not neccessary because file name is based on files that exist vs user input file
  #   print("That file does not exist")
  #   time.sleep(1)
  #   open_file_menu()
  
start_app()

#--------------------------------------------------------------------#
# This is going to be a new menu that allows you to create a new file
# def create_file():
#   #Need to figure out how to iterate over the file names to list them
#   File_name = input("Enter new file name:")
#   #maybe check to see if the the file ends with txt
#   file = open(File_name,'x')
# create_file()
#--------------------------------------------------------------------#
  # Select_From_Commands()
# def show_menus():
#   print("Select from an option below.")
#   time.sleep(1)
#   print()
#   print("- Open Budget")
#   time.sleep(1)
#   print("- Logout")
#   time.sleep(1)

#   while True:
#     Reply = input("Select an option from above.\n").lower()
#     if Reply == "open budget" or Reply == "openbudget":
#       open_file_menu()
#     elif Reply == "logout":
#       quit()
#     else:
#       #***********************************************#
#       # Need to add a way to delete the previous lines
#       #***********************************************#
#       print("Invalid command used.")
  
# show_menus()

# This function verifies the user
# def Verify_User():
#   attempts = 3
#   print("Welcome to Budget Buddy!")
#   time.sleep(2)
#   print("Create an account to access the tool.")
#   time.sleep(1)
#   #add a conditional to make sure the Username is the proper length
#   Username = input("Create a username.\n")
#   #add a conditional to make sure the Password is the proper length
#   Password = input("Create a password.\n")
#   print()
#   while attempts > 0: 
#     time.sleep(1)
#     print("Enter your login information")
#     print()
#     time.sleep(1)
#     UserField = input("Enter Username\n")
#     PasswordField = input("Enter Password\n")

#     time.sleep(1)

#     if UserField == Username and PasswordField == Password:
#       print("Welcome back ", Username)
#       show_menus()
#     elif attempts > 1: 
#       print()
#       print("Incorrect Username and Password Combination. \nTry again.\n")
#       attempts -= 1
#       print("You have", attempts, "attempts left.\n")
#     else: 
#       print("You have been locked out")
#       attempts -= 1


# Verify_User()
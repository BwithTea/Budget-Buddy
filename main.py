
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

import time
import os

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
def file_select(file_dict):
  while True:
    file_found = False
    # User inputs the number to the corresponding text file
    print("Select which file you would like to open.")
    Reply = str(input("Enter the file number.\n").lower())
    # Find the text file using their input
    for file in file_dict:
      
      if(file["num"] == Reply):
        file_found = True
        print("You are trying to open " ,file["name"])
        Reply = input("Confirm (y/n)").lower()
        if Reply == "yes" or Reply == "y":
          return file["name"]
        elif Reply != "no" and Reply != "n":
          print("Input not recognized.")
          continue
      
    if not file_found:
      print("File was not found")

    if not Reply.isdigit():
      print("Please input a number.")

#-----------------------------------------------------------
def create_list_of_bills(list_of_bills,file,FileName):
  good_format = False
  for line in file:
    # Splits line into a list
    data = line.strip().split(",")
    # Can change based on the main format of the file, currently three keys in dict
    if(len(data) == 3):
      print("You are working in ", FileName)
      good_format = True
      list_of_bills.append({'name':data[0],'date':data[1],'amount':data[2]})
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
    print("Would you like to add another bill?")
    Reply = input("Confirm (y/n)").lower()
    if Reply == "yes" or Reply == "y":
      continue
    elif Reply == "no" or Reply == "n":
      is_active = False
      
  

  
#----------------------------------------------#
def open_file_menu():
  list_of_bills = []
  curr_file_list = []
  file_dict = []
  file_dir_list = os.listdir()
  
  #pick a file to open
  print("Filename list:")
  
  #------------------------------------
  # These functions need to be put into separate helper functions
  # Add txt files to curr_file_list
  for file in file_dir_list:
    if file.find(".txt") != -1:
      curr_file_list.append(file)

  # List each file num and create a object based on name and num keys
  for i,file in enumerate(curr_file_list):
    file_dict.append({"name":file,"num":str(i+1)})

  # Print the files assigned number and name
  for file in (file_dict):
    print(file["num"] + "-" + file["name"])
  #---------------------------------------------------

  time.sleep(1)
  
  #------------------------------------------------------------
  # This return the file the user selected
  FileName = file_select(file_dict)
  #-------------------------------------------------------------
  
  try:
    #This needs to be put in a helper function 
    file = open(FileName,"r")
    
    list_of_bills = create_list_of_bills(list_of_bills,file,FileName)
    file.close()
    #-------------------------------------------------------------------
    if list_of_bills != []:
      print("Bills:")

    for line in list_of_bills:
      print(line)
    #-----------------------------------------#
    # Menu when the file is open
    print("Select an option from below.")
    print("- Add Bill")
    Reply = input("What would you like to do?").lower()
    if Reply == "add bill":
      add_bill(FileName)
    else:
      print("incorrect command input.")
    # Print each bill from list_of_bills

    print("Will that be the end of today's session?")
      
  except FileNotFoundError:
    # Not neccessary because file name is based on files that exist vs user input file
    print("That file does not exist")
    time.sleep(1)
    open_file_menu()
  
open_file_menu()

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
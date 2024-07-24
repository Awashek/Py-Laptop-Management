# Importing necessary modules
import operations
import read

# Displaying welcome message and contact information
print("----------------------------------------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\t\t\tWelcome to One Suppliers")
print("----------------------------------------------------------------------------------------------------------------------------------------------------")
print("\n")
print("Address : Mid-Baneshwor")
print("Contact no : 9829527434")
print("Shop Time : 24/7")

# Reading data from file and storing in a dictionary
product_dictionary = read.read()

# Running a loop until user exits
while(True):
    # Displaying options to the user
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\tHello Welcome to Admin Service.")
    print("\t\t\t\t\t\tPlease select any one options available below :)")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("(1) : Select 1 if you wish to place an order from the manufacturer.")
    print("(2) : Select 2 if you wish to sell computer to the customer.")
    print("(3) : Select 3 to leave the system.")
    print("\n")
    
    # Handling user input
    success=True
    while success==True:
        try:
            select = int(input("Which option would you like to select? \n ->"))
            success = False
        except:
            print("Invalid input!!")
            print("Please choose the available options.")
            print("\n")
    print("\n")
    
    if select == 1:
        #calling buy function from operations
       operations.buy(product_dictionary)
    
    elif select == 2:
        #calling sell function from operations
        operations.sell(product_dictionary)
       
    elif select == 3:
        print("Thank you for visiting us :)")
        break

    else:
        print("Invalid input!!")
        print("Please choose the available options." )
        print("")
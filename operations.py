# Importing necessary modules
from datetime import datetime
import write
import tab
import read


def add_bill(user_name,user_selected_laptops):
    """
    Print a bill for the selected laptops with the user name and purchase date and time.

    Args:
        user_name (str): The name of the user.
        user_selected_laptops (list): A list of tuples containing the details of the selected laptops.
            Each tuple contains four values in this order: laptop name, quantity, unit price, final price.

    Returns:
        None
    """
    present_day_and_time = datetime.now()
    # Printing the header of the bill
    print("\n")
    print("\n")
    print("\t\t\t\t\t\t\t\tOne Suppliers Bill")
    print("\n")
    print("Baneshwor, kathmandu  ") 
    print("Contact No: 9876567876") 
    print("\n")
    # Printing the details of the receipt

    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Details of the Receipt are:")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("Buyer Name: " + str(user_name))
    print("Purchase Date and time: "+str(present_day_and_time))
    print("\n")
    # Printing the purchase details
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Purchase Details are given below:")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("SN\t\tLaptop Name\t\tFinal Quantity\t\tUnit Price\t\tFinal Price")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    # Iterating through the selected laptops to print their details
    a = 1
    grand_final = 0
    for i in user_selected_laptops:
        grand_final += i[3]
        print(a, "\t\t" +i[0]+tab.tab(i[0])+"\t"+str(i[1])+tab.tab(str(i[1]))+"\t"+str(i[2])+tab.tab(str(i[2]))+"\t"+"$"+str(i[3])+tab.tab(str(i[3])))
        a +=1
        print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    # Calculating the VAT and gross amount
    vat = grand_final * 0.13
    amount_with_vat = grand_final + vat
    # Printing the net amount and gross amount
    print("Net Amount is:$"+str(grand_final))
    print("Gross Amount(amount with vat) is:$"+ str(amount_with_vat))
    


def sell_bill(user_name,user_number,user_selected_laptops,shipping_charge):
    """
    This function allows the user to buy a laptop by selecting the laptop ID and quantity.
    It updates the product stock and generates an invoice for the purchase.

    Args:
    product_dictionary (dictionary): A dictionary containing laptop details with their ID as key.

    Returns:
    None
    """
    present_day_and_time = datetime.now()
    # Print the header of the bill
    print("\n")
    print("\t\t\t\t\t\t\t\tOne Suppliers Bill")
    print("\n")
    print("Baneshwor, kathmandu  ") 
    print("Contact No: 9876567876")
    # Print the details of the receipt 
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Details of the Receipt are:")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("Name of the customer: "+str(user_name))
    print("Contact number: "+str(user_number))
    print("Purchase Date and time: "+str(present_day_and_time))
    print("\n")
    # Print the purchase details
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Purchase Details are given below:")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("SN\t\tLaptop Name\t\tFinal Quantity\t\tUnit Price\t\tFinal Price")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    # Print the details of each selected laptop
    a = 1
    grand_final = 0
    for i in user_selected_laptops:
        grand_final += i[3]
        print(a, "\t\t" +i[0]+tab.tab(i[0])+"\t"+str(i[1])+tab.tab(str(i[1]))+"\t"+str(i[2])+tab.tab(str(i[2]))+"\t"+"$"+str(i[3])+tab.tab(str(i[3])))
        a +=1
        print("----------------------------------------------------------------------------------------------------------------------------------------------------")

    # Add shipping charges if requested
    if shipping_charge == "Y":
        shipping_cost=25
        print("Your shipping charge is: ","$",str(shipping_cost))
        print("Net Amount :$"+str(grand_final + shipping_cost))
        print("!!Your shipping charge is added to Net Amount!!")
    else:
        print("Your Net Amount is :$"+str(grand_final))
    print("\n")

        
def buy(product_dictionary):
    """
    Allows the user to purchase laptops.
    Asks the user for their name, the ID and quantity of each laptop they want to purchase, and then generates an invoice.
    The user's details and the purchased laptops are added to the 'Invoice History' file and the stock levels are updated.
    
    Parameters:
    product_dictionary (dictionary): A dictionary containing the details of all laptops in stock
    
    Returns:
    None
    """
    # Ask the user to enter their name
    print("You have to enter your details first.")
    print("\n")
    user_name = input("Please enter your name:")
    # Validate user input for name
    while not user_name.isalpha():
        print("Invalid name!!")
        user_name = input("Please enter your name:")
    print("\n")
    # Prompt the user to select laptops to add to the stock
    add_order_again = "Y"
    user_selected_laptops = []
    while add_order_again == "Y" or add_order_again=="Yes" :   
         # Display the current stock details
        read.table()
        print("\n")
        # Prompt the user to enter the laptop ID and quantity
        print("Please provide the valid id and the quantity of the laptop which you would like to add to the stock?")
        print("\n")
        success=True
        while success==True:
            try:
                laptop_id = int(input("Please provide the ID of the laptop you want to add? \n -> "))  
                success = False
            except:
                print("Invalid laptop ID!!")
                print("Please provide the available id.") 
                print("\n")   
        print("\n")
        # Validate user input for laptop ID
        while laptop_id <= 0 or laptop_id > len(product_dictionary):
            print("Invalid laptop ID!!")
            print("Please provide the available id.")    
            print("\n")
            success=True
            while success==True:
                try:
                    laptop_id = int(input("Please provide the ID of the laptop you want to add? \n -> "))  
                    success = False
                except:
                    print("\n")
                    print("Please provide the id of the laptop here!!")
                    print("\n")
        success=True
        while success==True:
            try:    
                laptop_quantity = int(input("How many laptops would you like to add? \n -> " ))
                success = False
            except:
                print("\n")
                print("Please provide the quantity of the laptop here!!")
                print("\n")
                
        print("\n")
        
        # Validate user input for laptop quantity
        actual_quantity = product_dictionary[laptop_id][3]
        while laptop_quantity <= 0 or laptop_quantity > int(actual_quantity):
            print("not available")
            print("\n")
            success=True
            while success==True:
                try:    
                    laptop_quantity = int(input("How many laptops would you like to add? \n -> " ))
                    success = False
                except:
                    print("\n")
                    print("Please provide the quantity of the laptop here!!")
        # Update the stock details with the new laptops
        product_dictionary[laptop_id] [3] = int(product_dictionary[laptop_id][3]) + (laptop_quantity)
        
        write.update(product_dictionary)
        
        # Record user selected laptops for invoice generation
        product_name = product_dictionary[laptop_id][0]
        selected_quantity = laptop_quantity
        unit_price = product_dictionary[laptop_id][2]
        selected_laptop_price = product_dictionary[laptop_id][2].replace("$","")
        final_price = int(selected_laptop_price) * int(selected_quantity)
        
        user_selected_laptops.append([product_name,selected_quantity,unit_price,final_price])
        
        # Ask user if they want to add another laptop        
        add_order_again = input("Would you like to add another laptop ? (Press Y to add again.) \n ->" ).upper()
        while not add_order_again.isalpha():
            print("Invalid input!! Please enter Y or N ")
            add_order_again = input("Would you like to add another laptop ? (Press Y to add again.) \n ->" ).upper()
        print("\n")
    #calling the function add_bill for invoice in the shell
    add_bill(user_name,user_selected_laptops)
    
    #calling the function invoice_add from the write.py file for invoice in the text file
    write.invoice_add(user_name,user_selected_laptops)
    
    
def sell(product_dictionary):
    """
    Allows the user to sell laptops.
    Asks the user for their name, the ID and quantity of each laptop they want to purchase, and then generates an invoice.
    The user's details and the purchased laptops are added to the 'Invoice History' file and the stock levels are updated.
    
    Args:
    - product_dictionary: a dictionary containing information about the available laptops

    Returns:
    - None
    """
    print("You have to enter your detail of the customer first.")
    print("\n")
    # Get customer name and validate input
    user_name = input("Please enter Customer Name:")
    while not user_name.isalpha():
        print("Invalid customer name!!")
        user_name = input("Please enter Customer Name:")  
    print("\n")
    #Get customer number and validate input
    success=True
    while success==True:
        try:
            user_number = int(input("Please enter customer number:"))
            success=False
        except:
            print("You can only type your number here.")
            print("\n")
            
    order_again="Y"
    #Display available laptops and get user input for laptop ID
    user_selected_laptops = []
    while order_again=="Y"or order_again=="Yes":
        read.table()
        success=True
        while success==True:
            try:
                laptop_id = int(input("Please provide the ID of the laptop you want to buy? \n -> "))  
                success = False
            except:
                print("Invalid laptop ID!!")
                print("Please provide the available id.") 
                print("\n")   
        print("\n")
         # Validate laptop ID input
        while laptop_id <= 0 or laptop_id > len(product_dictionary):
            print("Invalid laptop ID!!")
            print("Please provide the available id.")    
            print("\n")
            success=True
            while success==True:
                try:
                    laptop_id = int(input("Please provide the ID of the laptop you want to buy? \n -> "))  
                    success = False
                except:
                    print("\n")
                    print("Please provide the id of the laptop here!!")
                    print("\n")
        success=True
        # Get user input for laptop quantity and validate input
        while success==True:
            try:    
                laptop_quantity = int(input("How many laptops would you like to order? \n -> " ))
                success = False
            except:
                print("\n")
                print("Please provide the quantity of the laptop here!!")
                print("\n")
                
        print("\n")
    
        
        actual_quantity = product_dictionary[laptop_id][3]
        # Validate laptop quantity input and check availability
        while laptop_quantity <= 0 or laptop_quantity > int(actual_quantity):
            print("not available")
            print("\n")
            success=True
            while success==True:
                try:    
                    laptop_quantity = int(input("How many laptops would you like to order? \n -> " ))
                    success = False
                except:
                    print("\n")
                    print("Please provide the quantity of the laptop here!!")
                # Update product dictionary with new laptop quantity
        product_dictionary[laptop_id] [3] = int(product_dictionary[laptop_id][3]) - (laptop_quantity)
        
        write.update(product_dictionary)
        # Calculate selected laptop price and add to user selected laptops list
        product_name = product_dictionary[laptop_id][0]
        selected_quantity = laptop_quantity
        unit_price = product_dictionary[laptop_id][2]
        selected_laptop_price = product_dictionary[laptop_id][2].replace("$","")
        final_price = int(selected_laptop_price) * int(selected_quantity)
        
        user_selected_laptops.append([product_name,selected_quantity,unit_price,final_price])
        # Ask user if they want to buy another laptop
        order_again = input("Would you like to buy another laptop ? (Press Y to buy again.) \n ->" ).upper()
        while not order_again.isalpha():
            print("Invalid input!! Please enter Y or N ")
            order_again = input("Would you like to buy another laptop ? (Press Y to buy again.) \n ->" ).upper()
        print("\n")
    # Ask user if they want to ship another laptop
    shipping_charge = input("Would you like to ship your laptop?(Press Y to ship.) \n ->" ).upper()
    while not shipping_charge.isalpha():
            print("Invalid input!! Please enter Y or N ")
            shipping_charge = input("Would you like to ship your laptop?(Press Y to ship.) \n ->" ).upper()
    #calling the function sell_bill for invoice in the shell
    sell_bill(user_name,user_number,user_selected_laptops,shipping_charge)
    #calling the function from write.py file for invoice in the textfile
    write.invoice_sell(user_name,user_number,user_selected_laptops,shipping_charge)


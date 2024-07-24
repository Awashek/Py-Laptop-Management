#Importing necessary modules
from datetime import datetime
import tab

def update(product_dictionary):
    """
    Update the product dictionary to the file 'laptop.txt'.
    
    Args:
    product_dictionary: a dictionary of laptops with their attributes
    
    Returns:
    product_dictionary: updated dictionary of laptops with their attributes
    """
    # open file in write mode
    file = open("laptop.txt", "w")
    # iterate over the values in the dictionary
    for values in product_dictionary.values():
        file.write(str(values[0])+ ","+ str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
        # write each value to the file, separated by commas
        file.write("\n")
    # close the file
    file.close()
    # return the updated dictionary
    return product_dictionary  


def invoice_add(user_name,user_selected_laptops):
    """
    This function generates an invoice for the laptops that the user has selected to purchase.
    
    Parameters:
    user_name (str): The name of the user
    user_selected_laptops (list): A list of laptops that the user has selected to purchase
    
    Returns:
    None
    """
     # creating a new file with the user's name
    file= open(str(user_name)+".txt","w")
    # getting the current date and time
    present_day_and_time = datetime.now()
    #writing header of the bill
    file.write("\n")
    file.write("\t\t\t\t\t\t\t\t\t\t\t\t\tOne Suppliers Bill")
    file.write("\n")
    file.write("Baneshwor, kathmandu  ") 
    file.write("\n")
    file.write("Contact No: 9876567876")
    file.write("\n") 
    file.write("----------------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    #writing details of receipt
    file.write("Details of the Receipt are:")
    file.write("\n")
    file.write("----------------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    #weiting name of the buyer
    file.write("Buyer Name: " + str(user_name))
    file.write("\n")
    file.write("Purchase Date and time: "+str(present_day_and_time))
    file.write("\n")
    file.write("----------------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    #writing ourchase detail
    file.write("Purchase Details are given below:")
    file.write("\n")
    file.write("----------------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("\n")
    file.write("----------------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("SN\t\tLaptop Name\t\tFinal Quantity\t\tUnit Price\t\tFinal Price")
    file.write("\n")
    file.write("----------------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    a = 1
    grand_final = 0
    for i in user_selected_laptops:
        # calculating the total cost of all laptops
        grand_final += i[3]
        file.write(str(a) + "\t\t" +i[0]+tab.tab(i[0])+"\t"+str(i[1])+tab.tab(str(i[1]))+"\t\t"+str(i[2])+tab.tab(str(i[2]))+"\t"+"$"+str(i[3])+tab.tab(str(i[3])))
        file.write("\n")
        a +=1
        file.write("\n")
        file.write("----------------------------------------------------------------------------------------------------------------------------------------------------")
        file.write("\n")
    file.write("\n")
    # calculating the VAT amount

    vat = grand_final * 0.13
    # calculating gross amount
    amount_with_vat = grand_final + vat
    # writing the total cost of all laptops
    file.write("Net Amount :$"+str(grand_final))
    file.write("\n")
    file.write("Gross Amount(amount with vat) is:$"+ str(amount_with_vat))
    # closing the file
    file.close()
    
    
def invoice_sell(user_name,user_number,user_selected_laptops,shipping_charge):
    """
    This function generates an invoice for a customer who has purchased laptops from One Suppliers.
    The invoice includes details such as customer name, contact number, purchase date and time, shipping charges (if applicable),
    and a list of purchased laptops with their details such as name, quantity, unit price, and final price.

    Parameters:

    user_name (str): the name of the customer
    user_number (int): the contact number of the customer
    user_selected_laptops (list): a list of tuples containing details of the selected laptops by the customer
    shipping_charge (str): a string indicating whether the customer wants to include shipping charges in the invoice (possible values are 'Y' and 'N')
    Returns:

    None
    The function opens a new file with a name that combines customer name and contact number and writes the invoice details into it.
    """
    present_day_and_time = datetime.now()
    file = open(str(user_name)+ str(user_number)+".txt","w")
    file.write("\n")
    file.write("\t\t\t\t\t\t\t\t\t\t\t\tOne Suppliers Bill")
    file.write("\n")
    file.write("Baneshwor, kathmandu  ") 
    file.write("\n")
    file.write("Contact No: 9876567876")
    file.write("\n") 
    file.write("\n") 
    file.write("----------------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n") 
    file.write("Details of the Receipt are:")
    file.write("\n") 
    file.write("----------------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n") 
    file.write("Name of the customer: "+str(user_name))
    file.write("\n") 
    file.write("Contact number: "+str(user_number))
    file.write("\n") 
    file.write("Purchase Date and time: "+str(present_day_and_time))
    file.write("\n") 
    file.write("\n")
    file.write("----------------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n") 
    file.write("Purchase Details are given below:")
    file.write("\n") 
    file.write("----------------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n") 
    file.write("\n")
    file.write("----------------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n") 
    file.write("SN\t\tLaptop Name\t\tFinal Quantity\t\tUnit Price\t\tFinal Price")
    file.write("\n") 
    file.write("----------------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n") 
    a = 1
    grand_final = 0
    for i in user_selected_laptops:
        grand_final+=i[3]
        file.write(str(a) + "\t\t" +i[0]+tab.tab(i[0])+"\t"+str(i[1])+tab.tab(str(i[1]))+"\t\t"+str(i[2])+tab.tab(str(i[2]))+"\t"+"$"+str(i[3])+tab.tab(str(i[3])))
        file.write("\n") 
        a +=1
        file.write("\n") 
        file.write("----------------------------------------------------------------------------------------------------------------------------------------------------")
        file.write("\n") 
    if shipping_charge == "Y":
        shipping_cost = 25
        file.write("\n") 
        file.write("Your shipping charge is:$"+str(shipping_cost))
        file.write("\n") 
        file.write("Net Amount :$"+str(grand_final + shipping_cost))
        file.write("\n") 
        file.write("!!Your shipping charge is added to Net Amount!!")
        file.write("\n") 
    else:
        file.write("\n") 
        file.write("Your Grand Final is :$"+str(grand_final))
    print("\n")
    file.close()
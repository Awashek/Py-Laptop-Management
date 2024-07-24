# Importing necessary modules
import tab
def read():
    """
    Reads the content of 'laptop.txt' file and creates a dictionary of products where each key is a unique product ID and
    each value is a list containing the product details (name, brand, price, quantity). The function returns the
    dictionary of products.

    Returns:
    - product_dictionary: A dictionary of products where each key is a unique product ID and each value is a list
    containing the product details (name, brand, price, quantity).
    """
    
    # Open the 'laptop.txt' file in read mode
    file = open("laptop.txt", "r")
    product_dictionary = {}
    
    # Initialize a counter to assign a unique ID to each product
    product_id = 1
    
    # Iterate through each line of the file
    for line in file:
        
        # Remove the newline character at the end of the line
        line = line.replace("\n","")
        
        # Split the line into a list of values separated by commas
        # and add it as a value in the dictionary with the current product ID as the key
        product_dictionary.update({product_id: line.split(",")})
        # Increment the product ID counter
        product_id +=1
    # Close the file

    file.close()  
    # Return the product dictionary
    return product_dictionary   


def table():
    """
    Read the laptop.txt file and create a dictionary where each key is the laptop ID and each value is a list
    containing the laptop details.

    Returns:
    product_dictionary (dict): A dictionary where each key is the laptop ID and each value is a list
    containing the laptop details.
    """
    # read the laptop data from the file
    product_dictionary = read()
    #
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Here's the list of the available laptops you can choose any you like.")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("S.N\t\tLaptop Name\t\tBrand\t\tPrice\t\tQuantity\t\tProcessor\t\tGraphic Card")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------") 
    #opens file  
    file = open("laptop.txt", "r")
    a = 1
    for i in product_dictionary.values():
        print(a, "\t\t" +i[0]+tab.tab(i[0])+"\t"+i[1]+tab.tab(i[1])+i[2]+tab.tab(i[2])+str(i[3])+tab.tab(str(i[3]))+i[4]+tab.tab(i[4])+"\t"+i[5]+tab.tab(i[5]))
        #increment a by 1
        a += 1
        print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    file.close()
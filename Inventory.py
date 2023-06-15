# Capstone project IV, inventory program using OOP

# Importing module 
from tabulate import tabulate

# Creating shoe class
class Shoes:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        print(self.cost)

    def get_quantity(self):
        print(self.quantity)

    def __str__(self):
        print(self.country, self.code, self.product, self.cost, self.quantity)

    def new_quantity(self, total):
        self.quantity = total


# Assigning variables
shoe_info = []
country = []
code = []
product = []
cost = []
quantity = []

# Function forreading shoe data
def read_shoe_data(country, code, product, cost, quantity):
    shoe = Shoes(country, code, product, cost, quantity) # Creating shoe object
    with open("inventory.txt", "r") as stock:
        for line in stock:
            line = line.split(',') # Splitting line by ',' so all info for a shoe is on one line
        for shoe in line:
            shoe = line
        shoe_info.append(shoe) # Appending shoe info to shoe list
        

# Function to capture new shoe details
def capture_shoes(country, code, product, cost, quantity):
    shoe_list = Shoes(country, code, product, cost, quantity) # Creating shoe list object
    print("Enter the following information regarding the shoe:") # requesting info from user
    country = input("Country:")
    code = input("Shoe code:")
    product = input("Shoe name:")
    cost = input("Price of shoe:")
    quantity = input("Quantity of shoe in stock:")
    shoe_list = "".join(country + ',' + code + ',' + product + ',' + cost + ',' + quantity) # Joining info 
    with open("inventory.txt", 'a') as new_shoe: # Opening file to add new shoe info 
        new_shoe.write('\n' + str(shoe_list)) # Writing new shoe info to text file
    print()
    print("Shoe details added succesfully.")

# Function to view all shoes in text file    
def view_all(country, code, product, cost, quantity):
    shoe = Shoes(country, code, product, cost, quantity)
    with open("inventory.txt", "r") as stock:
        for line in stock:
            line = line.split(',')
            for shoe in line:
                shoe = line
            shoe_info.append(shoe)
        print(tabulate(shoe_info))  # Displaying info in a table
    
# Function to re-stock shoe items
def re_stock(country,code, product, cost, quantity):
    details = [] # Creating variable
    par_level = int(input("Please enter the minimum stock level for shoe stock:")) # Request min stock level
    with open("Inventory.txt", "r") as stock:
        for line in stock:
            line = line.split(",")
            details.append(line)
    info = details[1:] # Removing first line from details variable, left with useful data
    shoe = Shoes(country, code, product, cost, quantity) # Creating shoe object
    for line in info: # For loops to run through details list, get correct info
        for item in line:   # Getting info to display in table
            country = line[0]
            code = line[1]
            product = line[2]
            cost = line[3]
            quantity = int(line[4])
        if quantity <= par_level: # Comparing stock levels lower or equal to par stock levels
            table = [["Country", "Code", "Product", "Cost", "Quantity"],
            [country, code, product, cost, quantity]]
            print(tabulate(table))  # Displaying shoe equal or lower than parstock levels entered
            add_stock = int(input("How many units do you want to add to this stock item?")) # Adding to stock
            shoe = Shoes(country, code, product, cost, quantity) # Shoe object to write info to file 
            total = quantity + add_stock
            shoe.new_quantity(total) # Assigning new stock value to shoe
            with open("Inventory.txt", "a") as update_stock:
                update_stock.write('\n' + str(shoe.country) + ',' + str(shoe.code) +',' + str(shoe.product)
                + ',' + str(shoe.cost)+ ',' +str(shoe.quantity)) # Updating on file
                print("Quantity added to shoe stock") # Informing user stock has been added
                print()    

# Function to search for shoes by their product code
def search_shoe(country, code, product, cost, quantity):
    headings = []
    with open("inventory.txt", "r") as stock:
        for line in stock:
            line = line.split(",")
            headings.append(line)
            info = headings[1:] # Saving useful data in variable
    shoe = Shoes(country, code, product, cost, quantity) # Creating object
    for line in info:   # Getting info to display in table
        country = line[0]
        code = line[1]
        product = line[2]
        cost = line[3]
        quantity = line[4]
    search = input("Enter the shoe code you are looking for:") # Requesting user info
    for shoe in info:
        if search == shoe[1]:
            table = [["Country", "Code", "Product", "Cost", "Quantity"], # Creating table
            [shoe[0], shoe[1], shoe[2], shoe[3], shoe[4]]] # Using indexing to display neatly            
    print()
    print(tabulate(table)) # Display information

# Function to calculate total value of each stock item
def value_per_item(product, cost, quantity):
    headings = []
    with open("inventory.txt", "r") as stock:
        for line in stock:
            line = line.split(",")
            headings.append(line)
            info = headings[1:] # Variable with useful data
    shoe = Shoes(country, code, product, cost, quantity) # Creating shoe object 
    for line in info:
        product = line[2]
        cost = line[3]
        quantity = line[4]
        total_value = int(cost) * int(quantity) # Casting to integers for calculating total value
        table = [["Product", "Total Value"],[product, total_value]] # Creating table
        print(tabulate(table)) # Displaying information
    

def highest_qty(country, code, product, cost, quantity):
    number = []
    headings = []
    with open("inventory.txt", "r") as stock:
        for line in stock:
            line = line.strip('\n') # Removing last character by stock levels
            line = line.split(",")
            headings.append(line)
            info = headings[1:]
            number.append(line[4])  # Adding stock quantities to list
    number.remove(number[0]) # Removing 'country' from list, left with numbers only
    maximum_number = (max(number, key=lambda value: int(value))) # Using lambda function, cast value to int
    shoe = Shoes(country, code, product, cost, quantity) # Shoe object
    for line in info:   # Gets information to display in table
        country = line[0]
        code = line[1]
        product = line[2]
        cost = line[3]
        quantity = line[4]
    for shoe in info:
        if maximum_number == shoe[4]: # Comparing stock levels to get highest shoe  in stock
            table = [["Country", "Code", "Product", "Cost", "Quantity"],
            [shoe[0], shoe[1], shoe[2], shoe[3], shoe[4]]] # Indexing to display in table neatly
    print()
    print("The following shoe is for sale:")  # Displaying to user
    print(tabulate(table))

# Main function with menu options and calling on other functions depending on selection.    
def main():
    menu_choice = "puma"
    while menu_choice != "nikey":
        print()
        menu_choice = input("""Enter one of the following menu options:
                        'capture' - Capture new shoe information
                        'view' - View all shoes in stock
                        'stock' - Add stock to shoes with low levels
                        'search' - Search for shoe by code
                        'value' - Get the total value of each shoe item in stock
                        'most' - Display shoe with highest stock level
                        'nikey' - Exit
                        :""")
        if menu_choice == "capture":
            capture_shoes(country, code, product, cost, quantity)
        elif menu_choice == "view":
            view_all(country, code, product, cost, quantity)
        elif menu_choice == "stock":
            re_stock(country, code, product, cost, quantity)
        elif menu_choice == "search":
            search_shoe(country, code, product, cost, quantity)
        elif menu_choice == "value":
            value_per_item(product, cost, quantity)
        elif menu_choice == "most":
            highest_qty(country, code, product, cost, quantity)
        elif menu_choice == "nikey":
            print()
            print("Have an air max wonderful day, goodbye.")
        else:
            print()
            print("You made an 'addidas' selection :( please try again.")

# Calling on function
main()

#https://pypi.org/project/tabulate/
#https://www.geeksforgeeks.org/python-program-to-find-largest-number-in-a-list/
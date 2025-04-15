#import necessary libraries
from datetime import datetime

#initialize variables and data structures

#create lists 
customers = [] #list to store the customer details
Colombo = [] #list to store the order details of Colombo branch (B001)
Nugegoda = [] #list to store the order details of Nugegoda branch (B002)
Piliyandala = [] #list to store the order details of Piliyandala branch (B003)
Gampaha = [] #list to store the order details of Gampaha branch (B004)

#string variables
cID = ""
name = ""
Bday = ""
address = ""
OrderID = ""
Bcode = ""
Date = ""
contact = ""
save = ""
ItemName = ""

#integer variables
choice = 0 #Store the main menu choice
Qnty = 0

#float variables
UnitPrice = 0.0
DailySales = 0.0

#boolean variables
Run = True #Variable to control the main menu loop

#loop to display the main menu after each operation
while Run:
    #display the main menu
    print ( "                       ABC Super Market")
    print ("\n** Main Menu **")
    print ("-----------------------------------\n")
    print ("1. Register a new customer")
    print ("2. Place an order")
    print ("3. View daily sales")
    print ("4. View customer details")
    print ("5. View order details")
    print ("6. Exit")
    print ("\n-----------------------------------\n")

    #get the user's choice
    choice = int(input("Enter your choice: "))
    print ("\n-----------------------------------")

    #check the user's choice and perform the corresponding operation
    if choice == 1:

        #register a new customer
        print ("\n                       ABC Super Market\n")
        print ("** Register a new customer **")
        print ("-----------------------------------\n")

        #get customer details

        while True:
            cID = input("Enter customer ID: ").strip().upper()

            #check if the ID is empty
            if not cID:
                print("\nCustomer ID cannot be empty.")

            #check if the ID exists
            elif cID in [customer[0] for customer in customers]:
                print("\nCustomer ID already exist. Please enter a differnt ID")
            
            #check if customer ID is valid
            elif len(cID) != 4 or cID[0] != 'C' or not cID[1:].isdigit():
                print("\nCustomer ID is invalid. Please enter a valid ID. (e.g., C001)")

            #end the loop if customer ID is valid
            else:
                break
        
        while True:
            name = str(input("Enter customer name: "))

            #check if customer name is valid
            if len(name) < 3 or len(name) > 20:
                print ("\nCustomer name is invalid. Please enter a valid name.")

            #end the loop if customer name is valid
            else:
                break

        while True:
            Bday = input("Enter customer birthday (YYYY-MM-DD): ")

            #check if birthday is valid
            try:
                datetime.strptime(Bday, "%Y-%m-%d")

                #end the loop if birthday is valid
                break

            #invalid date format
            except ValueError:
                print("\nInvalid date format. Please enter in YYYY-MM-DD format.")
        

        while True:
            address = str(input("Enter customer address: "))

            #check if address is valid
            if len(address) < 5 or len(address) > 100:
                print ("\nCustomer address is invalid. Please enter a valid address.")

            #end the loop if address is valid
            else:
                break

        while True:
            contact = str(input("Enter customer contact number: "))

            #check if contact number is valid
            if not contact.isdigit() or len(contact) != 10:
                print("\nContact number is invalid. Please enter a valid contact number (e.g., 0712345678).")

            #end the loop if contact number is valid
            else:
                break

        print ("\n-----------------------------------\n")

        #save the details
        while True:    
            save = str(input("Do you want to save the customer details (Yes/No)? ")).strip().upper()

            print('\n-----------------------------------')

            if save == "YES":
                customers.append((cID,name,Bday,address,contact))
                print ('\n* Saved successfully! *')
                break

            #not saving the details 
            elif save == "NO":
                print ("\n* Details were not saved. *")
                break
            
            #invalid input
            else:
                print("\nInvalid input. Please enter 'Yes' or 'No'.")
        
        print("\n-----------------------------------\n")

    elif choice == 2:

        #place an order
        print("\n                       ABC Super Market\n")
        print("** Place an Order **")
        print("-----------------------------------\n")

        #get order details
        while True:
            cID = input("Enter Customer ID: ").strip().upper()

            #check if the customer ID exists
            if cID in [customer[0] for customer in customers]:
                break
            else:
                print("\nCustomer ID not found. Please enter a valid Customer ID.\n")

        while True:
            Bcode = input("Enter Branch Code (B001, B002, B003, B004): ").strip().upper()

            #check if the branch code is valid
            if Bcode in ("B001", "B002", "B003", "B004"):
                break
            else:
                print("\nInvalid Branch Code! Please enter a valid Branch Code.\n")

        while True:
            Date = input("Enter Order Date (YYYY-MM-DD): ").strip()

            #check if the date format is correct
            try:
                datetime.strptime(Date, "%Y-%m-%d")
                break

            except ValueError:
                print("\nInvalid date format. Please try again.\n")

        while True:
            OrderID = input("Enter Order ID: ").strip().upper()

            #check if the Order ID is valid
            if len(OrderID) != 4 or OrderID[0] != 'O' or OrderID[1] != 'D' or not OrderID[2:].isdigit():
                print("\nOrder ID is invalid. Please enter a valid ID. (e.g., OD01)")

            else:
                break

        #initialize the lists
        order = [cID, Bcode, Date, OrderID]
        items = []
        Total = 0.0

        #add the first item
        while True:
            ItemName = input("Enter Item Name: ").strip()
            if len(ItemName) < 2:
                print("\nInvalid Item Name. Please enter a valid Item Name.\n")
            else:
                break

        while True:
            Qnty = int(input("Enter Quantity: "))
            if Qnty <= 0:
                print("\nQuantity cannot be 0 or lower\n")
            else:
                break
            

        while True:
            UnitPrice = float(input("Enter Unit Price: "))
            if UnitPrice <= 0:
                print("\nUnit Price cannot be 0 or lower\n")
            else:
                break


        #add the first item to the items list
        items.append((ItemName, Qnty, UnitPrice))
        Total = Total + (Qnty * UnitPrice)
        print("\nTotal Amount: ", Total)

        #ask if the user wants to add more items
        for i in range(2):
            while True:
                add_more = input("\nDo you want to add one more item? (yes/no): ").strip().upper()

                if add_more == "YES":
                    # get additional item details
                    while True:
                        ItemName = input("Enter Item Name: ").strip()
                        if len(ItemName) < 2:
                            print("\nInvalid Item Name. Please enter a valid Item Name.\n")
                        else:
                            break

                    while True:
                        Qnty = int(input("Enter Quantity: "))
                        
                        #check if the quantity is more than 0
                        if Qnty <= 0:
                            print("\nQuantity cannot be lower than 1.\n")
                        else:
                            break

                    while True:

                        #check if the unit price is lower than 0
                        UnitPrice = float(input("Enter Unit Price: "))
                        if UnitPrice <= 0:
                            print("\nUnit Price cannot be 0 or lower.\n")
                        else:
                            break

                    # Add the additional item to the items list
                    items.append((ItemName, Qnty, UnitPrice))
                    Total = Total + (Qnty * UnitPrice)
                    print("\nTotal Amount: ", Total)
                    break

                elif add_more == "NO":
                    # Exit the loop if the user doesn't want to add more items
                    break

                else:
                    print("\nInvalid input. Please enter 'YES' or 'NO'.\n")

            # Exit the outer loop if the user doesn't want to add more items
            if add_more == "NO":
                break

        #save the order
        print("\nOrder Details:")
        print ("\n-----------------------------------\n")
        print("Customer ID: ", cID)
        print("Branch Code: ", Bcode)
        print("Order Date : ", Date)
        print("Order ID   : ", OrderID)
        print("\nItems:")
        for item in items:
            print("Item Name: ", item[0], ", Quantity: ", item[1], ", Unit Price: ", item[2])

        #show the total amount
        print("\nTotal Order Value: ", Total)
        print ("\n-----------------------------------\n")

        #ask if the user wants to save the order
        while True:

            save = input("Do you want to save the order? (yes/no): ").strip().upper()

            if save == "YES":
                #save the order to the enterd branch
                if Bcode == "B001":
                    Colombo.append(order + items)
                elif Bcode == "B002":
                    Nugegoda.append(order + items)
                elif Bcode == "B003":
                    Piliyandala.append(order + items)
                elif Bcode == "B004":
                    Gampaha.append(order + items)

                print("\nOrder saved successfully!")
                print ("\n-----------------------------------\n")
                break
            
            #dont save the order
            elif save == "NO":
                print("\nOrder was not saved.")
                print ("\n-----------------------------------\n")
                break
            
            #invalid input
            else:
                print("\nInvalid input. Please enter 'YES' or 'NO'.\n")

    elif choice == 3:

        #view daily sales amount of a given branch
        print("\n                       ABC Supermarket\n")
        print("** View daily Sales amount **")
        print ("-----------------------------------\n")

        #looping until the user enters a valid branch code
        while True:
            Bcode = str(input("Enter Branch Code: ")).strip().upper()

            #checking if the branch code is valid
            if Bcode in ("B001", "B002", "B003", "B004"):
                break

            #if not re-enter the branch code.
            else:
                print("\nInvalid Branch Code! Please enter a valid Branch Code. (B001, B002, B003, B004)\n")

        #looping until user chooses to exit
        while True:
            
            #Initializing the variable
            DailySales = 0.0

            #enter the date
            Date = str(input("\nEnter Date(YYYY-MM-DD): "))

            #check if the date is in correct format
            try:
                datetime.strptime(Date,"%Y-%m-%d")
            except ValueError:
                print("\nInvalid date format.Please try again (YYYY-MM-DD)")
                continue

            #give branch name to the Bcode
            if Bcode == "B001":
                branch = Colombo
            elif Bcode == "B002":
                branch = Nugegoda
            elif Bcode == "B003":
                branch = Piliyandala
            elif Bcode == "B004":
                branch = Gampaha
            else:
                pass
            
           
            #checking the daily sales amount of the given branch
            for order in branch:

                #check if the order date matches and the order has items
                if order[2] == Date and len(order) > 4:

                    #calculate the total
                    for item in order[4:]:
                        DailySales = DailySales + (item[1] * item[2])

            #displaying the daily sales amount of the branch
            if DailySales <= 0.0:
                print("\nNo sales on ", Date)
                print ("\n-----------------------------------")

            else:
                print("\nTotal Sales amount on ", Date, " is: ", DailySales)
                print ("\n-----------------------------------")

            #looping until the user enters a valid input
            while True:

                #ssking the user if they want to check the sales amount of another date
                day = str(input("\nDo you want to check the sales amount of another date? (yes/no): ")).upper()

                #let the user input another date
                if day == "YES":
                    break
                
                #end this loop and continue to end 
                elif day == "NO":
                    break

                #invalid input
                else:
                    print("\nInvalid input! Please enter a valid input.(yes/no)")
            #if don't want to see sales in another date exit the outer loop
            if day == "NO":
                break

    elif choice == 4:

        #if customers list is empty
        if not customers:
            print("\nNo one has registered yet.\n")
            input("Press enter to return to the main menu.")
            

        else:
            #show the details of the customer
            print ("\n                       ABC Super Market\n")
            print ("** View Customer Details **")
            print ("-----------------------------------\n")
            
            while True:
                customer_id = input("Enter the customer ID (or type 'exit' to go back): ").strip().upper()

                #option to exit
                if customer_id == "EXIT":
                    print("\nReturning to the main menu...\n")
                    break

                #check if the ID is empty
                elif not customer_id:
                    print("\nCustomer ID cannot be empty. Please try again.\n")
                
                else:
                    customer_found = False
                    
                    for customer in customers:
                        if customer[0] == customer_id:
                            #show the details
                            print("\n-----------------------------------")
                            print("\nCustomer Details\n")
                            print("Customer ID : ", customer[0])
                            print("Name        : ", customer[1])
                            print("Birth Day   : ", customer[2])
                            print("Address     : ", customer[3])
                            print("Contact     : ", customer[4])
                            customer_found = True
                            break
                    
                    #if no customer was found
                    if not customer_found:
                        print("\nCustomer ID not found. Please enter a valid ID.\n")
                    else:
                        break 

        print("\n-----------------------------------\n")

    elif choice == 5:

        #view order details
        print("\n                       ABC Super Market\n")
        print("** View Order Details **")
        print("-----------------------------------\n")

        #check if there are any orders and return to the main menu
        if not (Colombo or Nugegoda or Piliyandala or Gampaha):
            print("\nNo orders have been placed yet.\n")
            input("Press Enter to return to the main menu...")
        else:
            while True:
                #get the Customer ID
                cID = input("Enter the Customer ID (or type 'exit' to go back): ").strip().upper()

                #exit if the user wants
                if cID == "EXIT":
                    print("\nReturning to the main menu.\n")
                    break

                #check if the input is empty
                elif not cID:
                    print("\nCustomer ID cannot be empty. Please try again.\n")
                else:
                    
                    orders_found = False

                    #search for orders in all branch lists
                    branches = [Colombo, Nugegoda, Piliyandala, Gampaha]
                    branch_names = ["Colombo", "Nugegoda", "Piliyandala", "Gampaha"]

                    for i in range(len(branches)):
                        branch = branches[i]
                        branch_name = branch_names[i]

                        #match the cID 
                        for order in branch:
                            if order[0] == cID:

                                #display the order details
                                print("\n-----------------------------------")
                                print("\nOrder Details\n")
                                print("Customer ID : ", order[0])
                                print("Branch Code : ", order[1])
                                print("Order Date  : ", order[2])
                                print("Order ID    : ", order[3])
                                print("\nItems:")

                                #print item name, quantity and unit price of the order
                                for item in order[4:]:
                                    print("Item Name: ", item[0], ", Quantity: ", item[1], ", Unit Price: ", item[2])

                                #initialize the total
                                Total = 0

                                #calculate total
                                for item in order[4:]:
                                    Total = Total + (item[1] * item[2])
                                print("\nTotal Order Value: ",Total)
                                print("\nBranch: ", branch_name)
                                print("\n-----------------------------------")
                                orders_found = True


                    #if no orders found
                    if not orders_found:
                        print("\nNo orders found for Customer ID: ", cID)
                    else:
                        print("\nAll orders for Customer ID: ", cID, " have been displayed.")
                        print("\n-----------------------------------")
                    #ask the user if they want to view another customer's orders
                    another_customer = input("\nDo you want to view orders for another customer? (yes/no): ").strip().upper()
                    if another_customer == "NO":
                        print("\nReturning to the main menu.\n")
                        break

    elif choice == 6:

        #exit the main program
        print("Exiting...\n")
        print("====================================\n")

        #end the main loop
        Run = False

    #invalid input
    else:
        print("\nInvalid input. Please select a number between 1 and 6.")

#show goodbye message after ending the program
print("  (: Thank You! Have a nice day :)")
print("\n====================================\n")

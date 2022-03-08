import mysql.connector as dbc

print("Welcome to RG Motor's Homepage.\n"
      "We have almost every car and bike you see on the Roads."
      "We have the finest quality of Automobiles.\n"
      "And with the help of our Engineers, you can customize to your expectations.\n"
      "Here, you can study the details of your next vehicle and to buy, you can contact the undersigned.")
print("")

connection = dbc.connect(host = 'localhost' ,
                         user = 'root' ,
                         password = 'rounaqbhasin' ,
                         database = 'rgmotors')
#To connect the program to Database


if connection.is_connected():
    pass

else:
    print("There is some error while connecting. Please try again!")
#To check if the program and database are connected

print("")
des = input("Are you a Customer or a Dealer? (D/C):")

if des.capitalize() == 'C':
    print("These are the Cars and Bikes we have dealt with.\n"
          "You may check the availability of the desired product and contact for further discussions.")
    print("")
    
    #The following code is for displaying 'Customer' table:
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM CUSTOMER;')
    data = cursor.fetchall()

    for row in data:
        print(row)

    print('')
    print("Contact Details:\n"
          "Mr. Pritam Sehgal\n"
          "Phone: 8851-09-2549\n"
          "Telephone: 011-4668-1510")

    print("")
    
    order = input("Would you like to order a Vehicle?(Y/N):")
    print("")
    #The following is for taking order from the user and putting it in 'order' table

    if order.capitalize() == 'Y':
        model = input("Enter the Model Name from the Table above:")
        
        colour = input("Enter the colour from the above given choices:")
        
        custom = input("What extra features would you like in your Vehicle:")
        
        name = input("Enter your good name:")
        
        if name == "": #To check if the 'Name' column is not empty
            name = input("It is necessary that you enter your Name:")
        else:
            pass
            
        num = int(input("Enter your phone number:"))
        
        date = int(input("Enter the delivery date of your product (Add 15 days from the date of delivery)(DDMMYY):"))

        cursor.execute("INSERT INTO booking VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(model, colour, custom, name, num, date))
        connection.commit()
        
        print("")
        print("Your order is placed. One of our Executive may call you for further proceedings.\n"
              "Thank You for your time and patience. :)")

    elif order.capitalize() == 'N':
        
        lack = input("Did you find the Vehicle of your choice?(Y/N)")

        if lack.capitalize() == 'Y':
            print("Thank You! Hope you liked our Service! :)")

        elif lack.capitalize() == 'N': #This block will add the info of the Vehicle which is not available at time:
            print('We apologize for the inconvenience for the same:\n'
                'You may complete the following Survey so that we can improve the future experience:')
            print('')

            name = input('Please enter your Good Name:(mandatory)')

            ph = int(input("Please enter your Phone Number:"))

            company = input("What is the name of the company of the Vehicle you're finding:")

            category = input("What type of Vehicle is it you're finding:")
            
            model = input("What is the Model Name of the Vehicle:")

            cursor.execute("INSERT INTO NEW VALUES('{}','{}','{}','{}','{}')".format(name, ph, company, category, model))

            print("Thank You for your response. We'll get back to you.")

    else:
        print("Wrong Command! Try Again.")

    
elif des.capitalize() == 'D':
    
    print("")
    print("Which table are you looking for?")
    print("1. Dealer's Directory\n"
          "2. Orders recieved\n")
    
    typ = int(input("Enter the no. of table you wish to see:"))
    
    if typ == 1:
            print("Good Day, Gentlemen! Below is the information regarding all the products that is present in your premises.")
            print("")


            #The following code is for displaying 'Dealer' table:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM DEALER;')
            data = cursor.fetchall()

            for row in data:
                print(row)

            print("")

            edit = input("Would you like to edit the database?(Y/N):")
            #To change the info in the database
                
            if edit.capitalize() == 'Y': 

                print("1. Model\n"
                        "2. Units\n"
                        "3. Cars bought this month\n"
                        "4. Default Colour\n")
                    
                change = int(input("What would you like to change?"))

                if change == 1: #To change Model Name
                    model1 = input("Enter the Model Name you want to change:")
                    model2 = input("Enter updated/new Model Name:")
                        
                    cursor.execute("UPDATE DEALER SET NAME ={} WHERE NAME ={}".format(model2, model1))
                    connection.commit()
                        
                elif change == 2: #To change no. of Units present
                    model = input("Enter the Model Name:")
                    unit = int(input("Enter the no. of Units available now:"))
                    cusore.execute("UPDATE DEALER SET UNITS = {} WHERE NAME = {}".format(unit, model))
                    connection.commit()
                        
                elif change == 3: #To change the no. of Cars bought this month
                    model = input("Enter the Model Name:")
                    shipped = int(input("Enter the number of cars bought in this month:"))

                    cursor.execute("UPDATE DEALER SET UNITS = {} WHERE NAME = {}".format(shipped1, shipped2))
                    connection.commit()
                        
                elif change == 4: #To change the available default colours
                    model = input("Input the default colour option:")
                    colour = input("Input the new default colour option:")

                    cursor.execute("UPDATE DEALER SET DEFAULT_COLOUR = {} WHERE NAME = {}".format(colour, model))
                    connection.commit()

                else:
                    print("Wrong Input! Please select a correct option.")
                    
            if edit.capitalize() == 'N':
                print("Okay! :)")
                             
    elif typ == 2:
        
        print("Good Day, Gentlemen!\n"
              "These are the Pending orders in our archive. You may begin with further proceedings ASAP.")
        print("")
        
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM BOOKING;')
        data = cursor.fetchall()

        for row in data:
            print(row)
            
else:
    print("Wrong Input! Terminating the Database...")

connection.close()
#To close the Database

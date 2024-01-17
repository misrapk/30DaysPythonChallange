#TODO: Task1: Login System 
users = ["vivek", "navneet", "priya", "harshit","shubham", "shreya"]

print("*** Welcome to LetsCode Shipping Panel ***")

user = input("Enter your username: ").lower().strip()


#TODO: Task2: Welcome Message 
if user in users:
    print(f"Hello {user}, Welcome Back in your account!\n")
    print("Current Shipping charges are below: ")
    #Task3: Display the charges
    print("Shipping Orders 0 to 100: \tRs.100/item")
    print("Shipping Orders 100 to 150: \tRs.80/item")
    print("Shipping Orders 150 to 200: \tRs.50/item")
    print("Shipping Orders more than 200: \tFree Delivery")
    #Task4: Input Number of items to ship 
    shipItems = int(input("How many items would you like to ship: "))
    
    #Calculate the shippment cost
    if shipItems <100:
        price = shipItems*100
    elif shipItems<150:
        price = shipItems*80
    elif shipItems<200:
        price = shipItems*50
    else:
        price = 0
    
    #TODO: Task5: Display the totla Shippment cost
    print(f"For {shipItems} items the shipping charges are Rs.{price}")
    
    confirmation = input("Would you like to place this order?(y/n)")
    if confirmation =='y':
        print(f"Thank you! Your order for {shipItems} items has been placed Successfully!")
    else:
        print("NO Order has been placed")
    
else:
    print("Sorry! you are not registered in our system. \nPlease create Account First")


 




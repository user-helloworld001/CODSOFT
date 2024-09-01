print("Welcome to Aman's Calculator, May you have a good experience.")
i=0
f="Y"
while(i==0 and f=="Y"):
    print("""Menu:
The List of Task which my Calculator can do are:
       1. Addition(Press 1 to Continue the process)
       2. Subtraction(Press 2 to Continue the process)
       3. Multiplication(Press 3 to Continue the process)
       4. Division(Press 4 to Continue the process)""")
    


    Choice= int(input("Enter The Number:"))


    if(Choice==1):


        First_Number=int(input("Enter the First Number: "))
        Second_Number=int(input("Enter the Second Number: "))
        Answer=First_Number+Second_Number
        print(Answer,"is the Sum of ", First_Number, "and ", Second_Number)
    
    
    
    if(Choice==2):



        First_Number=int(input("Enter the First Number: "))
        Second_Number=int(input("Enter the Second Number: "))
        Answer=First_Number-Second_Number
        print(Answer,"is the difference of ", First_Number, "and ", Second_Number)
    
    
    
    if(Choice==3):



        First_Number=int(input("Enter the First Number: "))
        Second_Number=int(input("Enter the Second Number: "))
        Answer=First_Number*Second_Number
        print(Answer,"is the product of ", First_Number, "and ", Second_Number)
    
    
    
    if(Choice==4):



        First_Number=int(input("Enter the First Number: "))
        Second_Number=int(input("Enter the Second Number: "))
        Answer=First_Number/Second_Number


        Quotient=First_Number//Second_Number
        Remainder=First_Number%Second_Number
    
        print(Answer,"is final answer for the division of ", First_Number, "and ", Second_Number)


        # Additional info
        print(Quotient,"is Quotient for the division of ", First_Number, "and ", Second_Number)
        print(Remainder,"is Remainder for the division of ", First_Number, "and ", Second_Number)
    
    f=input("""Do you want to continue?
Press Y to Continue and N to Close the Calculator.""")
    


    f=f.upper()
if(f=="N"):
    print("Thank You!! ")
    
    

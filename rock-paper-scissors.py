
import random


print("Welcome to Rock Paper Scissors Game!\n \n")
player_name=input("Player Name: ")

player_score=0
computer_score=0

Play_choice='Y'
while(Play_choice=='Y'):
    computer_choice=random.randint(1,3)


    print()
    print("""Press:
        1 for Rock
        2 for Paper
        3 for Scissors""")
    
    
    print()


    player_choice_str=input("Your Choice: ")



    while(player_choice_str==""):
           player_choice_str=input("Your Choice: ")



    player_choice=int(player_choice_str)
           


    while(player_choice>3 or player_choice<0):
           print("Invalid Input!")
           player_choice=int(input("Your Choice: "))



    while(player_choice==computer_choice ):
           print("Tie!")
           print("Your Score is",player_score)
           print("Computer Score is",computer_score)
           player_choice=int(input("Your Choice: "))
           computer_choice=random.randint(1,3)




    if(computer_choice==1 and player_choice==2):
            print(player_name," won.");
            player_score+=1;

    if(computer_choice==2 and player_choice==1):
            print("Computer won.");
            computer_score+=1;
    
    if(computer_choice==2 and player_choice==3):
            print(player_name," won.");
            player_score+=1;

    if(computer_choice==3 and player_choice==2):
            print("Computer won.");
            computer_score+=1;
    
    if(computer_choice==1 and player_choice==3):
            print("Computer won.");
            computer_score+=1;
    
    if(computer_choice==3 and player_choice==1):
            print(player_name," won.");
            player_score+=1;




    print()
    print("Computer Choice was",computer_choice)
    print("Your Choice was",player_choice)

    print()
    
    print("Your Score is",player_score)
    print("Computer Score is",computer_score)



    print()

    Play_choice=input("Do you want to continue? Press Y or N for your Answer:").upper()

    print()

    
    
    
if(Play_choice=='N'):
    
    print("Final Scores: ")
    print(player_name,": ",player_score)
    print("Computer : ",computer_score)

    print()
    print("Thank You For playing!")
    
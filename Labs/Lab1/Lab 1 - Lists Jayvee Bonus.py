#!/usr/bin/env python
# coding: utf-8

# # Lists
# 
# ## Background
# Lists are one of the most commonly used data structures in Python and are very similar to arrays from other programming languages. A list can store many items or values inside of one overall object or structure, unlike a variable which can only store one item or value inside one object. 
# 
# The items in a list can be accessed by using what is called an “index” value, which simply refers to the position of a certain item inside of a list, as lists are ordered from item 0 to the number of elements - 1. Therefore a list with 5 elements will have index positions 0 through 4. 
# 
# Any data can be stored inside a list, numbers, strings, or objects, but it is common practice to only have one data type per list. Therefore if my list has integers, it would ONLY have integers, not strings, doubles, objects, etc.

# ## Mini-project - Guessing game
# Create a number guessing game and set a secret number at the beginning of the program. 
# The program will ask the player to enter a number to guess what the number is, then it’ll inform the player if they got it right or wrong.

# In[1]:


secretnumber = 1
guess = int(input("make a guess"))
if guess == secretnumber:
    print ("omg you're so sexy aha")
else:
    print ("ehhh you're not that guy") #rude, but yes


# ## Mini-Project - Dice Roll
# 
# Part 1:
# Create a random number generator using dice. 
# You must create at least 5 dice
# The game must use conditionals (If, Else, Elif)
# The game must use nested conditionals (if 0=0:if 1=1: do something)
# 
# What lists should we create for the project?
# How many loops do we need?
# 
# Part 2:
# Create a list to store your gameplay. 
# Create at least 2 lists to store your game statistics.
# 
# Part 3:
# At the end of the output your gameplay statistics
# 
# Part 4:
# Exchange code with your partner and begin adding comments on improvements (save your original version)
# 
# Part 5:
# Return the code and create a comparison 
# 
# Part 6:
# Upload the code and comparison it to Canvas. 

# In[3]:


import random

def dice_face():
    list1 = [1, 2, 3, 4, 5, 6]
    return random.choice(list1) #we both used this form of dice roll instead of the random.ranint(1,6), def should use the latter

input("Press Enter to battle Megatron in dice roll...")
      
user_dice=dice_face()
computer_dice=dice_face()

print ("You rolled" , user_dice)
print ("Megatron rolled" , computer_dice)

if user_dice > computer_dice: 
    print ("You defeated Megatron")
elif user_dice < computer_dice: 
    print ("The Autobot resistance has failed")
else:
    print ("It's a draw, you both live to see another day")


# In[5]:


import random

print ("You dare face the mighty Megatron in a fiery game of dice roll?")
print ("Roll if you're feeling lucky kid!")

def dice_face():
    list1 = [1, 2, 3, 4, 5, 6]
    return random.choice(list1)

input("Press Enter to battle Megatron in dice roll...")
      
user_dice=dice_face()
computer_dice=dice_face()

list2 = (dice_face(), dice_face(), dice_face(), dice_face(), dice_face())
user_dice = list2
print ("You rolled :", user_dice)

list3 = (dice_face(), dice_face(), dice_face(), dice_face(), dice_face())
computer_dice = list3
print ("Megatron rolled :", computer_dice)


# In[7]:


if list2[0] > list3[0]:
    print ("Owww you injured the mighty Megatron")
elif list2[0] < list3[0]: 
    print ("Megatron has gained an advantage")
else: 
    print ("No one has advanced in this game")

if list2[1] > list3[1]:
    print ("Owww you injured the mighty Megatron")
elif list2[1] < list3[1]: 
    print ("Megatron has gained an advantage")
else: 
    print ("No one has advanced in this game")

if list2[2] > list3[2]:
    print ("Owww you injured the mighty Megatron")
elif list2[2] < list3[2]: 
    print ("Megatron has gained an advantage")
else:
    print ("No one has advanced in this game")

if list2[3] > list3[3]:
    print ("Owww you injured the mighty Megatron")
elif list2[3] < list3[3]: 
    print ("Megatron has gained an advantage")
else:
    print ("No one has advanced in this game")

if list2[4] > list3[4]:
    print ("Owww you injured the mighty Megatron")
elif list2[4] < list3[4]: 
    print ("Megatron has gained an advantage")
else:
    print ("No one has advanced in this game")


# In[9]:


print("--- Game Over ---")       
Finalscore_user = list2[0]+list2[1]+list2[2]+list2[3]+list2[4]
Finalscore_computer =list3[0]+list3[1]+list3[2]+list3[3]+list3[4] #i feel like theres a simpler way to do this, I did it the same way as Jayvee

if Finalscore_user > Finalscore_computer:
    print ("You've won, the Autobots have saved Cybertron!", Finalscore_user, Finalscore_computer)
elif Finalscore_user < Finalscore_computer:
    print ("You've lost, Cybertron has fallen...", Finalscore_user, Finalscore_computer)
else:
    print ("It's a draw, start over!", Finalscore_user, Finalscore_computer) #we worked together so our code is very similar


# ## Sample code
# Below you will find a Chat GPT generated Dice game.
# 
# Lets talk about it. 

# In[ ]:


import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Game!")
    print("You and the computer will each roll a dice, and the one with the higher number wins.")

    while True:
        input("Press Enter to roll the dice...")
        
        user_roll = roll_dice()
        computer_roll = roll_dice()

        print("You rolled:", user_roll)
        print("Computer rolled:", computer_roll)

        if user_roll > computer_roll:
            print("Congratulations! You win!")
        elif user_roll < computer_roll:
            print("Sorry, you lost. Better luck next time!")
        else:
            print("It's a tie!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





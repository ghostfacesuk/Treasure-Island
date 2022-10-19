print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n") 

junction = input('You have wandered for several hours down a beaten path and the trail splits here. Looking left you see a narrow gravel path heading towards a river. Looking right you see a stone path heading towards a clearing...\n\nGo "left" or go "right?"\n').lower()

if junction == str("left"):
    print("\nYou make your way down the narrow gravel path and reach the river. The current looks strong and the water seems deep. In the distance you hear movement coming from the dense woodland...")
else:
    print("\nYou make it to the clearing and look around... You hear a noise come from the bushes... A three headed demon dog jumps out and eats you alive!\n")
    input("\nGAME OVER YEAH!!!")
    exit()

junction = input('\n\nDo you "wait" or do you "cross" the river?\n').lower()

if junction == str("wait"):
    print("\nAs you wait you spot a small wooden brige in the far distance. You head over and cross the bridge. There is another trail which you decide to follow. The trail takes you to a giant stone wall. The wall has three doors all different in colour...")
else:
    print("\nYou move into the freezing cold river slowly making your way across. The current becomes too much to bear and you lose your footing on the river floor. The river takes you away and throws you off a waterfall...\n")
    input("\nGAME OVER YEAH!!!")
    exit()

junction = input('\n\nWhich door do you decide to try, "red", "blue", or "yellow"?\n').lower()

if junction == str("yellow"):
    print("You open the yellow door and find a massive chest of treasure. Well done!")
    input("\nGAME OVER YEAH!!!")
    exit()
else:
    print(f"You open the {junction} door and the floor falls! You have just triggered a trap and have fallen into a pit full of spikes!")
    input("\nGAME OVER YEAH!!!")
    exit()
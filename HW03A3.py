import random
stick = int(input("How many sticks (N) in the pile:"))
print('There are {} sticks in the pile'.format(stick))
name = input('What is your name :')
turn = random.randint(0, 1)  # 0 user play first, 1 bot play first
if turn == 0:
    print("####################\n{} play first\n####################".format(name))
else:
    print("###################\n Bot play first\n###################")
while (stick > 0):
    if turn == 0:
        pick = int(input("{}, how many sticks you will take (1 or 2) : ".format(name)))
        if pick != 1 or pick != 2:
            status = 1
        if (pick == 1 or pick == 2):  # normal cases, user follows the rule
            print(pick)
            stick -= pick
            turn = 1
            print("There is/are", stick, "stick(s) left in pile")
        else:
            print("You can pick only 1 or 2 stick!!")
            status = 0
            
    if turn == 1:
        if (stick + 2) % 3 == 1:
            print('I, smart computer, takes : 1 ')
            stick -= 1
            print("There is/are", stick, "stick(s) left in pile")
            turn = 0
        if (stick + 2) % 3 == 2:
            print('I, smart computer, takes : 2 ')
            stick -= 2
            print("There is/are", stick, "stick(s) left in pile")
            turn = 0
        if (stick + 2) % 3 == 0:
            bot = random.randint(1, 2)
            print('I, smart computer, takes : {}'.format(bot))
            stick -=bot
            print("There is/are", stick, "stick(s) left in pile")
            turn = 0
    
    
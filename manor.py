# Miranda LaBounty
# 9 May 2016

# Adventure game: MANOR HOUSE

# Explore the manor house to find you hamster Mr. Tibbles.
# Search rooms and its contents to find your hamster.
# Ask the house's inhabitants for advice or help when you come across them.

# VARIABLES


#dictionary of variables, by end of game all should be true.
dict_of_vars = {"findletter" : False, "missingkeys" : False, "newsforfather" : False, \
 "newsformother" : False, "newsforbutler" : False, "foundkeys" : False, \
 "keysformaid" : False, "checksunroom" : False, "opensunroom" : False}


# INTRO AND INSTRUCTIONS
def instructions():
    print "\n"
    print "You have just discovered that your hamster, Mr. Tibbles, has escaped your room \n" \
    "and hidden on the first floor of your house! You must find him!"
    print "Move through the house and check possible hiding spots in the rooms you find."
    print "Consider asking the inhabitants of the house for help, \nalthough sometimes they might" \
    " ask for a favor in return.\n"
    print "Use the command: here    to see what room you are in."
    print "Use the command: look    to see what is in the room around you."
    print "Use the command: check   to interact with a nearby item."
    print "Use the command: doors   to see which rooms you are adjacent too."
    print "Use the command: move    to go to a different room."
    print "Use the command: start   to return to your start point, the Front Hall."
    print "Use the command: help    to review these instructions."
    print "Use the command: quit    to exit the game."
    print "Now hurry! Before Mr. Tibbles gets away! \n"

#function to allow player to quit game
def quitgame():
    sure = raw_input("Are you sure you want to exit the game? Progress is not saved.\n")
    if sure == "yes":
        import sys
        sys.exit()
    else:
        pass


#admin transport, not for player use, just cause I got sick of
#moving one room at a time while testing this.
def transport():
    location = raw_input("Where. \n")
    if location == "mudroom":
        mudroom()
    elif location == "entryway":
        entryway()
    elif location == "powderroom":
        powderroom()
    elif location == "parlor":
        parlor()
    elif location == "fronthall":
        fronthall()
    elif location == "library":
        library()
    elif location == "study":
        study()
    elif location == "yourroom":
        yourroom()
    elif location == "classroom":
        classroom()
    elif location == "southhallway":
        southhallway()
    elif location == "masterbedroom":
        masterbedroom()
    elif location == "northhallway":
        northhallway()
    elif location == "guestroom":
        guestroom()
    elif location == "diningroom":
        diningroom()
    elif location == "sunroom":
        sunroom()
    else:
        print "nope"

#admin dictionary edit in-game, not for player, made for faster testing only
def adminflip():
    item = raw_input("What. \n")

    if item == "findletter true":
        dict_of_vars["findletter"] = True
    elif item == "findletter false":
        dict_of_vars["findletter"] = False

    elif item == "missingkeys true":
        dict_of_vars["missingkeys"] = True
    elif item == "missingkeys false":
        dict_of_vars["missingkeys"] = False

    elif item == "newsforfather true":
        dict_of_vars["newsforfather"] = True
    elif item == "newsforfather false":
        dict_of_vars["newsforfather"] = False

    elif item == "newsformother true":
        dict_of_vars["newsformother"] = True
    elif item == "newsformother false":
        dict_of_vars["newsformother"] = False

    elif item == "newsforbutler true":
        dict_of_vars["newsforbutler"] = True
    elif item == "newsforbutler false":
        dict_of_vars["newsforbutler"] = False

    elif item == "foundkeys true":
        dict_of_vars["foundkeys"] = True
    elif item == "foundkeys false":
        dict_of_vars["foundkeys"] = False

    elif item == "keysformaid true":
        dict_of_vars["keysformaid"] = True
    elif item == "keysformaid false":
        dict_of_vars["keysformaid"] = False

    elif item == "checksunroom True":
        dict_of_vars["checksunroom"] = True
    elif item == "checksunroom false":
        dict_of_vars["checksunroom"] = False

    elif item == "opensunroom true":
        dict_of_vars["opensunroom"] = True
    elif item == "opensunroom false":
        dict_of_vars["opensunroom"] = False



# ROOMS, STARTING AT SPAWN POINT


# front hall, start point and reset point
def fronthall():
    done = False
    while done != True:
        action = raw_input("You are in the Front Hall. \n")
        if action == "here":
            pass
        elif action == "look":
            print "There is no items in this room."
        elif action == "check":
            print "There is no items in this room."
        elif action == "doors":
            print "Adjacent rooms: \n north - South Hallway \n east - Library \
            \n south - Entryway \n west - Parlor"
        elif action == "move":
            move = raw_input("Direction? \n")
            if move == "north":
                southhallway()
            elif move == "east":
                library()
            elif move == "south":
                entryway()
            elif move == "west":
                parlor()
            else:
                print "There is no room in this direction."
        elif action == "start":
            fronthall()
        elif action == "help":
            instructions()
        elif action == "adtrans":
            transport()
        elif action == "adflip":
            adminflip()
        elif action == "quit":
            quitgame()
        else:
            print "Unrecognized command. Type help for commands."
    print "SOMETHING DIDNT WORK"

#south hallway
def southhallway():
    done = False
    while done != True:
        action = raw_input("You are in the South Hallway. \n")
        if action == "here":
            pass
        elif action == "look":
            print "Items: \n curtains"
        elif action == "check":
            check = raw_input("What would you like to check? \n")
            if check == "curtains":
                print "You look behind the heavy curtains but see no signs of Mr. Tibbles."
            else:
                print "That item is not in this room."
        elif action == "doors":
            print "Adjacent rooms: \n north - North Hallway \n east - Classroom \
            \n south - Front Hall \n west - Master Bedroom"
        elif action == "move":
            move = raw_input("Direction? \n")
            if move == "north":
                northhallway()
            elif move == "east":
                classroom()
            elif move == "south":
                fronthall()
            elif move == "west":
                masterbedroom()
            else:
                print "There is no room in this direction."
        elif action == "start":
            fronthall()
        elif action == "help":
            instructions()
        elif action == "adtrans":
            transport()
        elif action == "adflip":
            adminflip()
        elif action == "quit":
            quitgame()
        else:
            print "Unrecognized command. Type help for commands."
    print "SOMETHING DIDNT WORK"

#meeting room
def library():
    done = False
    while done != True:
        action = raw_input("You are in the Library. \n")
        if action == "here":
            pass
        elif action == "look":
            print "Items: \n chairs"
        elif action == "check":
            check = raw_input("What would you like to check? \n")
            if check == "chairs":
                print "You check the overstuffed armchairs around the room,"
                print "but the only thing you find is a handfull of loose change."
            else:
                print "That item is not in this room."
        elif action == "doors":
            print "Adjacent rooms: \n north - Classroom \n east - Study \n west - Front Hall"
        elif action == "move":
            move = raw_input("Direction? \n")
            if move == "east":
                study()
            elif move == "north":
                classroom()
            elif move == "west":
                fronthall()
            else:
                print "There is no room in this direction."
        elif action == "start":
            fronthall()
        elif action == "help":
            instructions()
        elif action == "adtrans":
            transport()
        elif action == "adflip":
            adminflip()
        elif action == "quit":
            quitgame()
        else:
            print "Unrecognized command. Type help for commands."
    print "SOMETHING DIDNT WORK"

#entryway
def entryway():
    done = False
    while done != True:
        action = raw_input("You are in the Entryway. \n")
        if action == "here":
            pass
        elif action == "look":
            print "Items: \n bench"
        elif action == "check":
            check = raw_input("What would you like to check? \n")
            if check == "bench":
                print "You crawl under the bench but only get a bump on your head for your efforts."
            else:
                print "That item is not in this room."
        elif action == "doors":
            print "Adjacent rooms: \n north - Front Hall \n east - Mud Room"
        elif action == "move":
            move = raw_input("Direction? \n")
            if move == "north":
                fronthall()
            elif move == "east":
                mudroom()
            else:
                print "There is no room in this direction."
        elif action == "start":
            fronthall()
        elif action == "help":
            instructions()
        elif action == "adtrans":
            transport()
        elif action == "adflip":
            adminflip()
        elif action == "quit":
            quitgame()
        else:
            print "Unrecognized command. Type help for commands."
    print "SOMETHING DIDNT WORK"

#mud room, letter telling uncle's arrival
def mudroom():
    done = False
    while done != True:
        action = raw_input("You are in the Mud Room. \n")
        if action == "here":
            pass
        elif action == "look":
            print "Items: \n coatrack \n paper"
        elif action == "check":
            check = raw_input("What would you like to check? \n")
            if check == "coatrack":
                print "You're not sure how Mr.Tibbles could have climbed up the coatrack,"
                print "But you check all the coat pockets just in case, but no hamster."
            elif check == "paper":
                print "You pick up Monday's newspaper."
                print "It must have gotten kicked in here and forgotten about."
                print "When you open it a letter falls out. You open the letter, it reads:"
                print " "
                print "  My dear brother,"
                print "  Due to an accident, my train got cancelled for this weekend."
                print "  Luckily they had an available ticket for Wednesday, so I'm take that one."
                print "  I'm sorry for the change in plans, and for arriving early."
                print "  I look forward to seeing you and your family."
                print "  Salutations."
                print " "
                print "Today is Wednesday! You should probably go tell your father the news \
                        when you get a chance."

                dict_of_vars["findletter"] = True

            else:
                print "That item is not in this room."
        elif action == "doors":
            print "Adjacent rooms: \n west - Entryway"
        elif action == "move":
            move = raw_input("Direction? \n")
            if move == "west":
                entryway()
            else:
                print "There is no room in this direction."
        elif action == "start":
            fronthall()
        elif action == "help":
            instructions()
        elif action == "adtrans":
            transport()
        elif action == "adflip":
            adminflip()
        elif action == "quit":
            quitgame()
        else:
            print "Unrecognized command. Type help for commands."
    print "SOMETHING DIDNT WORK"

#study, father inside, busy until uncle news
def study():
    done = False
    while done != True:
        action = raw_input("You are in the Study. \n")
        if action == "here":
            pass
        elif action == "look":
            if dict_of_vars["newsforfather"] == True:
                print "Items: \n desk \n bookshelf"
            else:
                print "Items: \n desk \n bookshelf"
                print "People: \n father"
        elif action == "check":
            check = raw_input("What would you like to check? \n")
            if check == "desk":
                print "Father doesnt like you going through his desk."
                print "Anyway, father would have surely noticed if Mr.Tibbles was in his desk."
            elif check == "bookshelf":
                print "You look through the book and underneath the shelf, but all you get is a"
                print "face full of dust. Achoo!"
            elif check == "father":
                if dict_of_vars["findletter"] == False:
                    print "I'm sorry dear but I haven't seen your little pet,"
                    print "now let me finish my work."
                elif dict_of_vars["newsforfather"] == False:
                    print "Oh my, my brother is arriving early? I'll have to go pick him up."
                    print "Please tell your mother the news. She's in her powder room."
                    dict_of_vars["newsforfather"] = True
                else:
                    print "Something went wrong. Dad should be gone, go fix it."
            else:
                print "That item is not in this room."
        elif action == "doors":
            print "Adjacent rooms: \n west - Library"
        elif action == "move":
            move = raw_input("Direction? \n")
            if move == "west":
                library()
            else:
                print "There is no room in this direction."
        elif action == "start":
            fronthall()
        elif action == "help":
            instructions()
        elif action == "adtrans":
            transport()
        elif action == "adflip":
            adminflip()
        elif action == "quit":
            quitgame()
        else:
            print "Unrecognized command. Type help for commands."
    print "SOMETHING DIDNT WORK"

# parlor, mother lounging
def parlor():
    done = False
    while done != True:
        action = raw_input("You are in the Parlor. \n")
        if action == "here":
            pass
        elif action == "look":
            print "Items: \n cabinet"
        elif action == "check":
            check = raw_input("What would you like to check? \n")
            if check == "cabinet":
                print "You look under the china cabinet but no Tr. Tibbles."
            else:
                print "That item is not in this room."
        elif action == "doors":
            print "Adjacent rooms: \n east - Front Hall \n south - Powder Room"
        elif action == "move":
            move = raw_input("Direction? \n")
            if move == "east":
                fronthall()
            elif move == "south":
                powderroom()
            else:
                print "There is no room in this direction."
        elif action == "start":
            fronthall()
        elif action == "help":
            instructions()
        elif action == "adtrans":
            transport()
        elif action == "adflip":
            adminflip()
        elif action == "quit":
            quitgame()
        else:
            print "Unrecognized command. Type help for commands."
    print "SOMETHING DIDNT WORK"

#powder room
def powderroom():
    if dict_of_vars["newsforfather"] == True:
        done = False
        while done != True:
            action = raw_input("You are in the Powder Room. \n")
            if action == "here":
                pass
            elif action == "look":
                if dict_of_vars["newsformother"] == False:
                    print "Items: \n couch \n mirror"
                    print "People: \n mother"
                else:
                    print "Items: \n cabinet \n mirror"
            elif action == "check":
                check = raw_input("What would you like to check? \n")
                if check == "couch":
                    print "Mother would have noticed if a hamster had joined her on the couch!"
                elif check == "mirror":
                    print "You admire yourself in the mirror, but then go back to searching."
                elif check == "mother":
                    if dict_of_vars["newsformother"] == False:
                        print "Hello darling. Your Uncle is early?"
                        print "Oh goodness. I must to get dressed for dinner then."
                        print "Tell the butler to get the guestroom ready when you get a chance."
                        dict_of_vars["newsformother"] = True
                    else:
                        pass
                else:
                    print "That item is not in this room."
            elif action == "doors":
                print "Adjacent rooms: \n north - Parlor "
            elif action == "move":
                move = raw_input("Direction? \n")
                if move == "north":
                    parlor()
                else:
                    print "There is no room in this direction."
            elif action == "start":
                fronthall()
            elif action == "help":
                instructions()
            elif action == "adtrans":
                transport()
            elif action == "adflip":
                adminflip()
            elif action == "quit":
                quitgame()
            else:
                print "Unrecognized command. Type help for commands."
        print "SOMETHING DIDNT WORK"
    else:
        print "Mother does not like being disturbed without reason."
        print "I should leave her alone for now."


#classroom
def classroom():
    done = False
    while done != True:
        action = raw_input("You are in the Classroom. \n")
        if action == "here":
            pass
        elif action == "look":
            print "Items: \n chalkboard \n desks"
        elif action == "check":
            check = raw_input("What would you like to check? \n")
            if check == "chalkboard":
                print "All you see on the whiteboard is the unicorn jousting tournament"
                print "that you drew on it yesturday. Your tutor was less than pleased."
            elif check == "desks":
                print "You check under the desks but it seen Mr. Tibbles is as interested"
                print "in studying as you are, and decided to avoid this room."
            else:
                print "That item is not in this room."
        elif action == "doors":
            print "Adjacent rooms: \n south - Library \n east - Your Room \n west - South Hallway"
        elif action == "move":
            move = raw_input("Direction? \n")
            if move == "south":
                library()
            elif move == "east":
                yourroom()
            elif move == "west":
                southhallway()
            else:
                print "There is no room in this direction."
        elif action == "start":
            fronthall()
        elif action == "help":
            instructions()
        elif action == "adtrans":
            transport()
        elif action == "adflip":
            adminflip()
        elif action == "quit":
            quitgame()
        else:
            print "Unrecognized command. Type help for commands."
    print "SOMETHING DIDNT WORK"

# your room, pushes back to classroom
def yourroom():
    print "You already checked in here for Mr. Tibbles, so you see no reason to stay."
    print "You decide to leave and continue your search."
    classroom()

# Master bedroom
def masterbedroom():
    done = False
    while done != True:
        action = raw_input("You are in the Master Bedroom. \n")
        if action == "here":
            pass
        elif action == "look":
            if dict_of_vars["newsformother"] == False:
                print "Items: \n bed \n vanity"
            else:
                print "Items: \n bed \n vanity"
                print "People: \n mother"
        elif action == "check":
            check = raw_input("What would you like to check? \n")
            if check == "bed":
                print "You look under the bed but only see a few of your father's old"
                print "socks. You sniff one and imediatley regret it."
            elif check == "vanity":
                print "A lot of tins of mother's makeup, but no hamsters."
            elif check == "mother":
                if dict_of_vars["newsformother"] == True:
                    print "I don't have time to talk about your pet."
                    print "I need to finish my makeup before your uncle arrives."
                else:
                    pass
            else:
                print "That item is not in this room."
        elif action == "doors":
            print "Adjacent rooms:\n east - South Hallway "
        elif action == "move":
            move = raw_input("Direction? \n")
            if move == "east":
                southhallway()
            elif move == "west":
                masterbedroom()
            else:
                print "There is no room in this direction."
        elif action == "start":
            fronthall()
        elif action == "help":
            instructions()
        elif action == "adtrans":
            transport()
        elif action == "adflip":
            adminflip()
        elif action == "quit":
            quitgame()
        else:
            print "Unrecognized command. Type help for commands."
    print "SOMETHING DIDNT WORK"


# North Hallway, butler until father tells to clear guest bedroom
def northhallway():
    done = False
    while done != True:
        action = raw_input("You are in the North Hallway. \n")
        if action == "here":
            pass
        elif action == "look":
            if dict_of_vars["newsforbutler"] == False:
                print "Ites: \n vase"
                print "People: \n butler"
            else:
                print "Items: \n vase"
        elif action == "check":
            check = raw_input("What would you like to check? \n")
            if check == "vase":
                print "You look in the huge vase, you lean in so far you almost fall in!"
                print "You manage to catch yourself and confirm there is no Mr. Tibbles."
            elif check == "butler":
                if dict_of_vars["newsforbutler"] == True:
                    pass
                elif dict_of_vars["newsformother"] == True:
                    print "The guestrooms need to be prepared? I'll get right to it."
                    dict_of_vars["newsforbutler"] = True
                else:
                    print "I dont have time for your little games right now."
                    print "Talk to me when you have something important to tell me."

            else:
                print "That item is not in this room."
        elif action == "doors":
            print "Adjacent rooms:\n east - Guestroom\n south - South Hallway\n north - Dining Room"
        elif action == "move":
            move = raw_input("Direction? \n")
            if move == "east":
                guestroom()
            elif move == "south":
                southhallway()
            elif move == "north":
                diningroom()
            else:
                print "There is no room in this direction."
        elif action == "start":
            fronthall()
        elif action == "help":
            instructions()
        elif action == "adtrans":
            transport()
        elif action == "adflip":
            adminflip()
        elif action == "quit":
            quitgame()
        else:
            print "Unrecognized command. Type help for commands."
    print "SOMETHING DIDNT WORK"

# Guest room
def guestroom():
    if dict_of_vars["newsforbutler"] == True:
        done = False
        while done != True:
            action = raw_input("You are in the Guest Room. \n")
            if action == "here":
                pass
            elif action == "look":
                if dict_of_vars["newsforbutler"] == False:
                    print "Items: \n bed \n wardrobe"
                else:
                    print "Items: \n bed \n wardrobe"
                    print "People: \n butler"
            elif action == "check":
                check = raw_input("What would you like to check? \n")
                if check == "bed":
                    print "The bed has an ugly yellow and blue comforter on it."
                    print "You feel sorry for your uncle for having to use it."
                    print "You are sure Mr. Tibbles has better taste than to be "
                    print "hiding under such ugly linens."
                elif check == "wardrobe":
                    print "You check under the wardrobe for Mr.Tibbles."
                    print "He isn't there, but you do see something shiny."
                    print "You grab it and see it is a ring of keys."
                    if dict_of_vars["missingkeys"] == True:
                        print "These must be the keys the maid lost."
                        print "You should bring them back to her."
                        dict_of_vars["foundkeys"] = True
                    else:
                        print "You decide to leave them there since you don't know who's they are."
                elif check == "butler":
                    if dict_of_vars["newsforbutler"] == True:
                        print "I need to get this clean, I can't talk right now."
                    else:
                        pass
                else:
                    print "That item is not in this room."
            elif action == "doors":
                print "Adjacent rooms:\n west - North Hallway"
            elif action == "move":
                move = raw_input("Direction? \n")
                if move == "west":
                    northhallway()
                else:
                    print "There is no room in this direction."
            elif action == "start":
                fronthall()
            elif action == "help":
                instructions()
            elif action == "adtrans":
                transport()
            elif action == "adflip":
                adminflip()
            elif action == "quit":
                quitgame()
            else:
                print "Unrecognized command. Type help for commands."
        print "SOMETHING DIDNT WORK"
    else:
        print "It's locked."

# dining room
def diningroom():
    done = False
    while done != True:
        action = raw_input("You are in the Dining Room. \n")
        if action == "here":
            pass
        elif action == "look":
            print "Items: \n table"
            print "People: \n maid"
        elif action == "check":
            check = raw_input("What would you like to check? \n")
            if check == "table":
                print "You peer under the heavy wood table but don't see anything interesting."
            elif check == "maid":
                if dict_of_vars["foundkeys"] == False:
                    print " You can't find your new hamster? Oh my."
                    print " I'd love to help but I need to find my keys,"
                    print " I dropped them while cleaning and need to find them."
                    print " If you find them, I may be able to give you a hand."
                    dict_of_vars["missingkeys"] = True

                elif dict_of_vars["keysformaid"] == True and dict_of_vars["checksunroom"] == True:
                    print " You say you can't get into the sunroom?"
                    print " Here is the right key. I'll get it back from you later."
                    dict_of_vars["opensunroom"] = True

                elif dict_of_vars["foundkeys"] == True:
                    print " Oh lovely! My keys!"
                    print " You say I dropped them in the guestroom? How silly of me."
                    print " Tell me if you want to look in a locked room."
                    dict_of_vars["keysformaid"] = True

                else:
                    "Something went wrong, go fix it."
            else:
                print "That item is not in this room."
        elif action == "doors":
            print "Adjacent rooms:\n east - Sunroom \n south - North Hallway"
        elif action == "move":
            move = raw_input("Direction? \n")
            if move == "south":
                northhallway()
            elif move == "east":
                sunroom()
            else:
                print "There is no room in this direction."
        elif action == "start":
            fronthall()
        elif action == "help":
            instructions()
        elif action == "adtrans":
            transport()
        elif action == "adflip":
            adminflip()
        elif action == "quit":
            quitgame()
        else:
            print "Unrecognized command. Type help for commands."
    print "SOMETHING DIDNT WORK"

# Sunroom
def sunroom():
    if dict_of_vars["opensunroom"] == True:
        done = False
        while done != True:
            action = raw_input("You are in the Sunroom. \n")
            if action == "here":
                pass
            elif action == "look":
                print "People: \n grandmother"
            elif action == "check":
                check = raw_input("What would you like to check? \n")
                if check == "grandmother":
                    print "Your grandmother sits on a floral couch, petting something"
                    print "you can't see in her lap."
                    print "Hello my dear."
                    print "I woke up from my nap and found this little guy on the ground beside me."
                    print "Isn't this your hamster, Mr. Tibbles?"
                    win()
                else:
                    print "That item is not in this room."
            elif action == "doors":
                print "Adjacent rooms:\n west - Dining room"
            elif action == "move":
                move = raw_input("Direction? \n")
                if move == "west":
                    diningroom()
                else:
                    print "There is no room in this direction."
            elif action == "start":
                fronthall()
            elif action == "help":
                instructions()
            elif action == "adtrans":
                transport()
            elif action == "adflip":
                adminflip()
            elif action == "quit":
                quitgame()
            else:
                print "Unrecognized command. Type help for commands."
        print "SOMETHING DIDNT WORK"
    else:
        print "It's locked. Maybe the maid has the key."
        dict_of_vars["checksunroom"] = True

def win():
    print "WIN AND STUFF"
    #ADD WIN STUFF

def main():

    instructions()

    fronthall()


if __name__ == "__main__":
    main()



"""

STORY LINE

You are a child going around your home trying to find your pet hamster. There are other
inhabitants of your house: FATHER, MOTHER, MAID, BUTLER, and GRANDMOTHER.

There are 15 rooms in your house: MUDROOM, ENTRYWAY, POWDER ROOM, PARLOR, FRONT HALL, LIBRARY, STUDY,
YOUR ROOM, CLASSROOM, SOUTH HALLWAY, MASTER BEDROOM, NORTH HALLWAY, GUESTROOM, DINING ROOM, SUNROOM. 

FATHER      : STUDY         -> out of house 
MOTHER      : POWDER ROOM   -> MASTER BEDROOM
MAID        : DINING ROOM   
BUTLER      : NORTH HALLWAY     -> GUEST ROOM
GRANDMOTHER : SUNROOM       

At start FORBIDDEN ROOMS are the MASTER BEDROOM, GUESTROOM, GUESTBATH, SUNROOM.

Start statements:
FATHER  : "I'm sorry dear but I havent seen your little pet, now let me finish my work."
MOTHER  : (cant enter room until spoken to FATHER)
MAID    : "I'd love to help but I need to find my keys, I dropped them while cleaning and 
            need to find them. If you find them, I may be able to give you a hand."
BUTLER  : "I dont have time for your little games right now. Talk to me when you have something 
            important to tell me."
GRANDMOTHER: (Cant enter room until got maid's keys.)


FATHER CHANGES:
    Auto:   
        "I'm sorry dear but I haven't seen your little pet, now let me finish my work."
    once read LETTER 
        "Oh my, my brother is arriving early? I'll have to go pick him up. 
         Please tell your MOTHER the news. She's in her POWDER ROOM.
then disappears from study and house.

MOTHER CHANGES:
    Auto:
        none. Cant enter powder room.
    in powder room, once read LETTER then talked to FATHER. ~only once~ 
        "Hello darling. Your Uncle is early? Oh goodness. I must to get dressed for dinner then. 
         Tell the BUTLER to get the GUEST ROOM ready when you get a chance.
    mother moves from POWER ROOM to MASTER BEDROOM.
    in master bedroom, once read LETTER then spoken to FATHER then MOTHER(1).
        "I don't have time to talk about your pet. I need to finish my makeup before your uncle arrives."

MAID CHANGES:
    Auto:
        "I'd love to help but I need to find my keys, I dropped them while cleaning and 
         need to find them. If you find them, I may be able to give you a hand."
    once found KEYS in GUESTROOM ~only once~
        "Oh lovely! My keys! You say I dropped them in the guestroom? How silly of me. Tell me if 
         you want to look in a locked room."
    once found KEYS in GUESTROOM and talked to MAID and tried to enter SUNROOM
        "You say you can't get into the sunroom? Here is the right key. I'll get it back from you later."

BUTLER CHANGES:
    Auto:
        "I dont have time for your little games right now. Talk to me when you have something 
         important to tell me."
    once found LETTER and spoken to FATHER and MOTHER
        "The guestrooms need to be prepared? I'll get right to it.
    moves to GUESTROOM
    when in GUESTROOM
        "I need to get this clean, I can't talk right now."

GRANDMOTHER CHANGES:
    AUTO:
        none
    once got access to SUNROOM from MAID
        "Hello my dear. I woke up from my nap and found this little guy on the ground beside me. 
         Isn't this your hamster, Mr. Tibbles?"


STORYLINE

-searches house for a time.
-may at any time speak to MAID in DINING ROOM and learn she lost her keys.
-finds LETTER in MUDROOM under PAPER 
-tells FATHER about news of UNCLE'S arrival learned in LETTER
-FATHER tells you to inform your MOTHER of the news, who is in the POWDER ROOM
-can now enter POWDER ROOM 
-tell MOTHER the news, who asks you to tell the BUTLER to prepare the GUESTROOM
-MOTHER moves to the MASTER BEDROOM
-tell BUTLER your MOTHER's instructions
-can now enter GUESTROOM
-find KEYS under WARDROBE in GUESTROOM
-bring KEYS to MAID in DININGROOM
-MAID thanks you and tells you to come back if you need a room opened
-you discover the SUNROOM is locked at some point
-ask MAID to open SUNROOM
-can now enter SUNROOM
-find GRANDMOTHER in SUNROOM with MR. TIBBLES 


VARIABLES:

findletter
    once found letter in mudroom when checking paper. allows convo with father about uncle.
missingkeys
    once spoken to maid for first time and heard she dropped her keys. allows finding keys in guestroom.
newsforfather
    after findletter=true. once told father uncle is coming early. allows entering powderroom. removes father from map.
newsformother
    after newsforfather=true. once told mother uncle is coming. allows giving instructions to butler. moves mother to masterbedroom.
newsforbutler
    after newsformother=true. once told butler to clean guestroom. opens guestroom.
foundkeys
    after missingkeys=true. after newsforbutler=true. once found keys under wardrobe in guestroom. allows givning keys to maid.
keysformaid
    after foundkeys=true. once given keys to the maid in the diningroom. allow to ask maid to open sunroom once attemp to enter.
checksunroom
    anytime. once attempt to enter sunroom and found locked. allows asking maid to open sunroom once keysformaid=true.
opensunroom
    after keysformaid=true and checksunroom=true. once asked maid to open sunroom. allows entry to sunroom.


            ________   ________
           |        | |        |
           | DINING |-| SUN    |
           | ROOM   |-| ROOM   |
           |________| |________| 
               ||               
            ________   ________
           |        | |        |
           | NORTH  |-| GUEST  |
           | HALL   |-| ROOM   |
           |________| |________| 
               ||                     
 ________   ________   ________   ________
|        | |        | |        | |        |
| MASTER |-| SOUTH  |-| CLASS  |-| YOUR   |
| BEDROOM|-| HALL   |-| ROOM   |-| ROOM   |
|________| |________| |________| |________|
               ||         ||          
 ________   ________   ________   ________
|        | |        | |        | |        |
| PARLOR |-| FRONT  |-| LIBRARY|-| STUDY  |
|        |-| HALL   |-|        |-|        |
|________| |________| |________| |________|
    ||         ||         
 ________   ________   ________
|        | |        | |        |
| POWDER | | ENTRY  |-| MUDROOM|
| ROOM   | | WAY    |-|        |
|________| |________| |________|

"""
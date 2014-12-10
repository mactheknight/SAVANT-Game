
                # Introduction / Preface

print "SAVANT"
print "_____________________________________________________________________________________________________________________________________"
print "You are Caspian, a knight of the Balthazarian Table. You are pale, tall, and lanky; your arms resembling noodles."
print "The king's daughter, Princess Amber, has been stolen away by a cruel, menacing dragon who goes by the name of Emrys."
print "The palace is in ruins and complete chaos has taken over with the uproar of the Princess' disappearance."
print "You, being the weakest knight, have been foolishly tricked by the other knights to embark on the quest to save the Princess, alone."
print "Your journey begins on foot, into the deepest and darkest dungeon in all of oblivion . . ."
print "_____________________________________________________________________________________________________________________________________"

                # Start Room - Essential

inventory = []
    
def startRoom():
    global inventory
    print "Entering the dungeon sword in hand, you see a deceased knight slumped against the wall still clutching his shield." 
    print "It's obviously no use to him anymore . . ."
    print "_____________________________________________________________________________________________________________________________________"
    userInput = raw_input()
    if userInput == "get shield" or userInput == "shield":
        addToInventory("shield")
        print "You picked up the shield !"
    else:
        print "_____________________________________________________________________________________________________________________________________"
        print "You leave the shield with the respected cadaver."
    print inventory
    print "The only exits available are west and east."
    print "_____________________________________________________________________________________________________________________________________"

def addToInventory(item):
    inventory.append(item)
    
startRoom()

                # East Room & West Room

userInput1 = raw_input()
                
if userInput1 == "east":
    global inventory
    print "_____________________________________________________________________________________________________________________________________"
    print "The east room is dim enough to see. The stones on the far wall look ready to crumble, as if something is wedged in between them."
    print "Hidden between the stones in the wall was a torch !"
    addToInventory("torch")
    print inventory
    print "There is nothing else in this room."
    print "The only available exit is to turn back to where you began."
    print "_____________________________________________________________________________________________________________________________________"
    userInput2 = raw_input()
    if userInput2 == "turn back":
        print "_____________________________________________________________________________________________________________________________________"
        print "You have returned to where you started."
        print "The only exit remaining is west."
        print "_____________________________________________________________________________________________________________________________________"
        userInput1 = raw_input()
if userInput1 == "west":
    print "_____________________________________________________________________________________________________________________________________"
    print "The west room is pitch black, you can't see anything."
    print "_____________________________________________________________________________________________________________________________________"
    userInput2 = raw_input()
    if userInput2 == "use torch":
        print "_____________________________________________________________________________________________________________________________________"
        print "You see a creature, the creature sees you."    
        print "The creature kills you !"
        print "GAME OVER." 
        print "_____________________________________________________________________________________________________________________________________"
    if userInput2 == "consider":
        print "_____________________________________________________________________________________________________________________________________"
        print "You can hear a creature shuffling somewhere within the room. You sneak past it quietly into the next room and a stone door permanently seals the path you came from, leaving you in a room with seemingly no exits."
        print "_____________________________________________________________________________________________________________________________________"
        userInput1 = raw_input()
        if userInput1 == "up":
                print "_____________________________________________________________________________________________________________________________________"
                print "Looking desperately for an exit you glance and notice a rope hanging down from the pitch black abyss that is the cieling."
                print "Your only chance of escape is to climb the rope, and so you do."
                print "After pulling yourself up the rope with your noodle arms for what seems like forever you reach an opening in the wall which you lean over to and abandon the rope."
                print "The final room is another pitch black room. However this time you hear the tingling of coins or something metallic as they rustle and bounce off of the stone floors."
                print "Fire illuminates the room, straight from the jaw of Emrys the ancient and menacing dragon."
                print "You spot Princess Amber from across the great hall of loot and gems that is the den Emrys resides in."
                print "She is unconscious. Before you can make any movement, everything becomes pitch black once again as you have been snatched into the jaws of Emrys, the shield proving useless and realisticaly teaching you the valuable life lesson that a human is no match for a dragon." 
                print "Pfsh, what were you thinking you pleb. You weren't even a wizard."
                print "_____________________________________________________________________________________________________________________________________"
                print "GAME OVER."
        else: 
                print "_____________________________________________________________________________________________________________________________________"
                print "There are no exits !"
                print "GAME OVER."
                print "_____________________________________________________________________________________________________________________________________"


   
        
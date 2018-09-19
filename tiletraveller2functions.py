"""With functions
1. i think implementation 1 was easier for me to write because that am better and faster writing without functions today.
2. after i wrote implementation 2(wich took a long time) i think that I2 is much cleaner and much better readable 
mainly because nr 1 was 78 lines but nr 2 is 
3. i was able to make 3 functions. the main function wich is 

"""
def changespilabord(direction, spilabord):
    if direction == "n":
                spilabord[1] += 1
    elif direction == "s":
                spilabord[1] -= 1
    elif direction == "e":
                spilabord[0] += 1
    elif direction == "w":
                spilabord[0] -= 1
    return spilabord
def getDirection(n, s, w, e):
    direction = (input("Direction: ")).lower()
    while direction != n and direction != s and direction != w and direction != e:
        print("Not a valid direction!")
        direction = (input("Direction: ")).lower()
    return direction

def main():
    spilabord = [1, 1]
    while spilabord != [3,1]: # sigurkassinn
        if spilabord == [1,1] or spilabord ==[2,1]:
            print("You can travel: (N)orth.")
            changespilabord(getDirection("n", "", "", ""), spilabord)    
        elif spilabord == [1,2]:
            print("You can travel: (N)orth or (E)ast or (S)outh.")
            changespilabord(getDirection("n", "s", "", "e"), spilabord)
        elif spilabord == [1,3]:
            print("You can travel: (E)ast or (S)outh.")          
            changespilabord(getDirection("", "s", "", "e"), spilabord)
        elif spilabord == [2,3]:
            print("You can travel: (E)ast or (W)est.")         
            changespilabord(getDirection("", "", "w", "e"), spilabord)
        elif spilabord == [3,3] or spilabord ==[2,2]:
            print("You can travel: (S)outh or (W)est.")           
            changespilabord(getDirection("", "s", "w", ""), spilabord)
        elif spilabord == [3,2]:
            print("You can travel: (N)orth or (S)outh.")           
            changespilabord(getDirection("n", "s", "", ""), spilabord)
    print("Victory!")

main()
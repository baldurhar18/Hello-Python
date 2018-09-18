#algrim
#gera upphafsstaðsetningu
#skilgreina hvernig hann hreyfir sig í gegnum kassana með upp,niður og hliðar tökkum
#nota while lykkju 
#búa til hvernig hver kassi fyrir sig er(hvernig er hægt að hreyfa sig í honum The player enters:
#• n/N for north (up)
#• e/E for east (right)
#• s/S for south (down)
#• w/W for west (left)
# prenta út victory ef hann lendir í lokakassanum 
locationx=1
locationy=1
location = [locationx, locationy]
while location != [3,1]:
    location = [locationx, locationy]
    if location == [1,1] or location ==[2,1]:
        print("You can travel: (N)orth.")
        while True:
            locationchange = input("Direction: ")
            if locationchange == "n":
                locationy += 1
                break
            else:
                print("Not a valid direction!")
    
    elif location == [1,2]
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        while True
            locationchange = (input("Direction: "))
            if locationchange.lower() == "n":
                locationy += 1
            elif locationchange.lower() == "e":
                locationx +=1
            elif locationchange.lower() == "s":
                locationx -= 1
            else:
                print("Not a valid direction!")
    
    
    
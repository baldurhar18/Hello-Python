#algrim
#gera upphafsstaðsetningu
locationx=1
locationy=1
#skilgreina hvernig hann hreyfir sig í gegnum kassana með upp,niður og hliðar tökkum
#nota while lykkju 
#búa til hvernig hver kassi fyrir sig er(hvernig er hægt að hreyfa sig í honum The player enters:
#• n/N for north (up)
#• e/E for east (right)
#• s/S for south (down)
#• w/W for west (left)
# prenta út victory ef hann lendir í lokakassanum 
while locationx !=3 or locationy !=1:
    if locationx == 1 and locationy==1 or locationx==2 and locationy==1:
        print("You can travel: (N)orth.")
        locationchange = (input("Direction: "))
        if locationchange.lower() == "n":
            locationy += 1
        else:
            print("Not a valid direction!")
    
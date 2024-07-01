techville = ["library", "techpark", "roundabout"]
roundabout = ["hospital", "mall", "airport", "university", "stadium"]

def start_engine():
    print("starting engine")

def move_forward():
    print("moving forward")

def turn(direction):
    print(f"turning {direction}")

def stop_engine():
    print("stopping engine")

def which_place():
    place = input("Where do you want to go? ").replace(' ','').lower()
    return place

def navigation(place):
    if place in techville:
        if place == 'library':
            move_forward()
            turn('left')
            print(f'We arrived at the {place.capitalize()}!')
        elif place == 'techpark':
            move_forward()
            turn('right')
            print(f'We arrived at the {place.capitalize()}!')
        elif place == 'roundabout':
            move_forward()
            print('We arrived at the Roundabout, now choose:')
            place = which_place()
            navigation(place)
    elif place in roundabout:
        if place == 'hospital':
            follow_roundabout(1)
            print(f'We arrived at the {place.capitalize()}!')
        elif place == 'mall':
            follow_roundabout(2)
            move_forward()
            turn('right')
            print(f'We arrived at the {place.capitalize()}!')
        elif place == 'airport':
            follow_roundabout(3)
            print(f'We arrived at the {place.capitalize()}!')
        elif place == 'university' or 'stadium':
            follow_roundabout(4)
            move_forward()
            if 'university':
                turn('left')
                print(f'We arrived at the {place.capitalize()}!')
            else:
                turn('right')
                print(f'We arrived at the {place.capitalize()}!')
    else:
        print(f'{place} is not in Techville')

def follow_roundabout(exit_number):
    move_forward()
    print('Entering the roundabout')
    print(f"taking exit number {exit_number} from the roundabout")


start_engine()
place = which_place()
navigation(place)
stop_engine()
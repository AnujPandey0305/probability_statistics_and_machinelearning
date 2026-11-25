import random

def simulate_game(switch):
    car_door = random.randint(1,3)
    initial_choice = random.randint(1,3)
    doors = [i for i in range(1,4) if i != car_door and i != initial_choice]
    host_door = random.choice(doors)
    if switch == "Switch":
        new_doors = [i for i in range(1,4) if i != initial_choice and i != host_door]
        new_door = new_doors[0]
    else:
        new_door = initial_choice
    return new_door == car_door
        

    
 
count_when_switch = 0

for i in range(100000):
    if simulate_game("Switch"):
        count_when_switch += 1

wr_switch = count_when_switch / 100000
print("Win rate when switching: ", wr_switch * 100)

count_when_no_switch = 0

for i in range(100000):
    if simulate_game("Do not Switch"):
        count_when_no_switch += 1

wr_no_switch = count_when_no_switch / 100000
print("Win rate when no switching: ", wr_no_switch)

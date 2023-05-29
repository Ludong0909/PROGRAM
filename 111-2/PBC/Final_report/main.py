import class_and_function as c
import numpy as np 
import matplotlib.pyplot as mp 

# Opening
print('Hello! We are group 43 of Programming of Business Computing!')
name = input('Welcome to the survial game! Input your character name please: ')

# Print_delay_time setting
delay_time_1 = 0.01
delay_time_2 = 0.005

# Introduction and instruction
c.print_with_delay('===================Rule instruction===================',delay_time_1)
c.print_with_delay('Hello, '+name+'. You are trapped on an isolated island. After 10 days, a helicopter will come and rescue you.',delay_time_2)
c.print_with_delay('You need to try to survive on this island by yourself before the helicopter arrive. Try your best to survive on this dangerous place until day 10!',delay_time_2)
print('')
c.print_with_delay('===================Resource instruction===================',delay_time_1)
c.print_with_delay('From now on, you have to collect and use 4 kind of resources: water, food, material and medkit.',delay_time_2)
c.print_with_delay('Water and food can help you increase your body state.',delay_time_2)
c.print_with_delay('If your shelter is damaged, you\'ll need material to repair it.',delay_time_2)
c.print_with_delay('If your health points drop, you can use medkit to heal yourself.',delay_time_2)
print('')
c.print_with_delay('===================Action instruction===================',delay_time_1)
c.print_with_delay('You can take an action everyday.',delay_time_2)
c.print_with_delay('1. If you go to explore, you can get some resources but you\'ll feel thirsty and hungry. Meanwhile the durability of your shelter will decrease too.',delay_time_2)
c.print_with_delay('2. If you decide to repair your shelter today, you\'ll consume 20 materials and your shelter\'s durability will increase 10 points. Your state will drop also.',delay_time_2)
c.print_with_delay('3. You can also do nothing today, but every state will drop slightly.',delay_time_2)
print('')
c.print_with_delay('===================Weather instruction===================',delay_time_1)
c.print_with_delay('There are 4 kinds of weather on this island: Sunny, cloudy, thunderstrom and cold.',delay_time_2)
c.print_with_delay('If it\'s sunny, you\'ll waste more thirst if you go out to explore or repair your shelter.',delay_time_2)
c.print_with_delay('If it\'s cloudy, nothing will happen.',delay_time_2)
c.print_with_delay('If it\'s thunderstrom, your thirst will add to 100 directly but you can\'t go out to explore today. Meanwhile, your shelter will drop more durability if you do nothing.',delay_time_2)
c.print_with_delay('If it\'s cold, your hunger will drop more. But your thirst will drop less.',delay_time_2)
print('')
c.print_with_delay('===================Supply instruction===================',delay_time_1)
c.print_with_delay('Don\'t forget that you can use food/water/medkit at the beginning of the day.',delay_time_2)
c.print_with_delay('Food will increase your hunger 12 points, water will increase your thirst 10 points, and medkit will increase your health 10 points.',delay_time_2)
print('')
c.print_with_delay('======================================================',delay_time_1)
c.print_with_delay('If your hunger or thirst is lower than 40, then your health will start to drop.',delay_time_2)
c.print_with_delay('If your shelter durability or your health drop to 0, you\'ll die and lose the game.',delay_time_2)
c.print_with_delay('If you survive 10 days successfully, you win the game!',delay_time_2)
c.print_with_delay('You can start the game after you read all the instructions, Good luck!',delay_time_2)

# Initial survival state
alive = True 
shelter = True
health = 100
thirst = 100
hunger = 100
shelter_hp = 100 
day = 0

# Initial supplies
medkit = c.medkit(1)
food = c.food(2)
water = c.water(4)
material = c.material(10)

# Weather system
weather = ['Sunny','Thunderstorm','Cold','Cloudy']

# Create arrays for plotting below
medkit_quantity = []
water_quantity = []
food_quantity = []
material_quantity = []
health_array = []
thirst_array = []
hunger_array = []
shelter_health_array = []

# Main loop 
while alive and shelter:
    day = day + 1 
    today_weather = c.random_weather(weather)
    print('===============Day '+str(day)+'===============')
    print('It\'s '+today_weather+' today!')
    if today_weather == 'Thunderstorm':
        thirst = 100
    if day == 10: # Condition to win this game
        c.print_with_delay('Congratulation! You\'ve been rescued from this harsh environment! You are a survival master!!',delay_time_2)
        break

    c.print_with_delay('-----Current state-----',delay_time_2)
    print('Health: '+str(health))
    print('Thirst: '+str(thirst))
    print('Hunger: '+str(hunger))
    print('Shelter durability: '+str(shelter_hp))
    c.print_with_delay('-----Current resources-----',delay_time_2)
    print('Water: '+str(water.get_quantity()))
    print('Food: '+str(food.get_quantity()))
    print('Material: '+str(material.get_quantity()))
    print('Medkit: '+str(medkit.get_quantity()))
    print('--------------------')
    
    while True: # Supplies consuming 
        c.print_with_delay('What supplies do you want to use? ',delay_time_2)
        c.print_with_delay('=====Using supplies=====',delay_time_1)
        c.print_with_delay('1: Water',delay_time_1)
        c.print_with_delay('2: Food',delay_time_1)
        c.print_with_delay('3: Medkit',delay_time_1)    
        c.print_with_delay('4: No need to use now',delay_time_1)
        c.print_with_delay('5: Show current state',delay_time_1)
        c.print_with_delay('6: Show current resources',delay_time_1)
        action = input('Please input number 1 ~ 6: ')
        if action.isdigit() == False:
            print('Wrong input!')
            continue
        elif action == '1' and water.get_quantity() > 0:
            water.consume_water(1)
            thirst = thirst + 10
            if thirst >= 100:
                thirst = 100
            print('Your thirst now is '+str(thirst)+'.')
        elif action == '2' and food.get_quantity() > 0:
            food.consume_food(1)
            hunger = hunger + 12
            if hunger >= 100:
                hunger = 100
            print('Your hunger now is '+str(hunger)+'.')
        elif action == '3' and medkit.get_quantity() > 0:
            medkit.consume_medkit(1)
            health = health + 10
            if health >= 100:
                health = 100
            print('Your health now is '+str(health)+'.')
        elif action == '4':
            break
        elif action == '5':
            c.print_with_delay('-----Current state-----',delay_time_2)
            print('Health: '+str(health))
            print('Thirst: '+str(thirst))
            print('Hunger: '+str(hunger))
            print('Shelter durability: '+str(shelter_hp))
        elif action == '6':
            c.print_with_delay('-----Current resources-----',delay_time_2)
            print('Water: '+str(water.get_quantity()))
            print('Food: '+str(food.get_quantity()))
            print('Material: '+str(material.get_quantity()))
            print('Medkit: '+str(medkit.get_quantity()))
        else:
            print('Wrong input or you don\'t have enough supplies!')
            continue

    while True: # Today's action
        c.print_with_delay('What action you want to take today?',delay_time_2)
        c.print_with_delay('1: Go out to explore.',delay_time_1)
        c.print_with_delay('2: Repair shelter.',delay_time_1)
        c.print_with_delay('3: Nothing.',delay_time_1)
        action = input('Please input number 1 ~ 3: ')
        if action == '1':
            if today_weather == 'Thunderstorm':
                c.print_with_delay('You can\'t go out to explore when the weather is thunderstorm!',delay_time_1)
                continue
            food.add_food(c.random_number(0,2))
            water.add_water(c.random_number(0,3))
            medkit.add_medkit(c.random_number(0,1))
            material.add_material(c.random_number(5,10))
            if today_weather == 'Sunny':
                hunger = hunger - c.random_number(15,25)
                thirst = thirst - c.random_number(25,35)
                shelter_hp = shelter_hp - c.random_number(10,20)   
                break
            elif today_weather == 'Cold':
                hunger = hunger - c.random_number(25,30)
                thirst = thirst - c.random_number(10,15)
                shelter_hp = shelter_hp - c.random_number(10,20)   
                break
            hunger = hunger - c.random_number(15,25)
            thirst = thirst - c.random_number(20,25)
            shelter_hp = shelter_hp - c.random_number(10,20)
            break
        elif action == '2' and material.get_quantity() >= 20:
            material.consume_material(20)
            shelter_hp = shelter_hp + 10
            if shelter_hp >= 100:
                shelter_hp = 100
            if today_weather == 'Sunny':
                hunger = hunger - c.random_number(12,25)
                thirst = thirst - c.random_number(25,35)  
                break
            if today_weather == 'Cold':
                hunger = hunger - c.random_number(25,30)
                thirst = thirst - c.random_number(10,15)
            hunger = hunger - c.random_number(12,25)
            thirst = thirst - c.random_number(15,25)
            break
        elif action == '3':
            if today_weather == 'Thunderstorm':
                shelter_hp = shelter_hp - c.random_number(20,30)
                break
            if today_weather == 'Cold':
                hunger = hunger - c.random_number(20,25)
                thirst = thirst - c.random_number(8,15)
                shelter_hp = shelter_hp - c.random_number(10,15)
                break
            hunger = hunger - c.random_number(10,20)
            thirst = thirst - c.random_number(15,20)
            shelter_hp = shelter_hp - c.random_number(10,15)
            break
        else:
            print('Wrong input or you don\'t have enough material!')
            continue
    
    # Lower limit of state
    if hunger < 0:
        hunger = 0
    if thirst < 0:
        thirst = 0

    # Health decreasing
    if thirst <= 10 or hunger <= 10:
        health = health - c.random_number(30,45)
    elif (thirst <= 20 and thirst > 10) or (hunger <= 20 and hunger > 10):
        health = health - c.random_number(25,40)
    elif (thirst <= 30 and thirst > 20) or (hunger <= 30 and hunger > 20):
        health = health - c.random_number(20,35)
    elif (thirst <= 40 and thirst > 30) or (hunger <= 40 and hunger > 30):
        health = health - c.random_number(15,30)
        
    # Condition for losing game 
    if health <= 0:
        c.print_with_delay('You died...',delay_time_2)
        alive = False
    if shelter_hp <= 0:
        c.print_with_delay('Your shelter has been destroyed.',delay_time_2)
        shelter = False
    
    # Collect data (unit:[day])
    medkit_quantity.append(medkit.get_quantity())
    water_quantity.append(water.get_quantity())
    food_quantity.append(food.get_quantity())
    material_quantity.append(material.get_quantity())
    health_array.append(health)
    thirst_array.append(thirst)
    hunger_array.append(hunger)
    shelter_health_array.append(shelter_hp)

    continue

if day == 10:
    x = np.linspace(1,day-1,day-1)
else:
    x = np.linspace(1,day,day)
f,(ax1,ax2) = mp.subplots(1,2,figsize=(15,9))

ax1.grid(color='tab:grey',linestyle=':',linewidth=0.5)
ax1.plot(x,health_array,color='tab:red')
ax1.plot(x,thirst_array,color='tab:blue')
ax1.plot(x,hunger_array,color='tab:orange')
ax1.plot(x,shelter_health_array,color='green')
ax1.set_xticks(np.linspace(1,9,9))
ax1.set_yticks(np.linspace(0,100,11))
ax1.set_xlim([1,9])
ax1.set_ylim([-5,101])
ax1.legend(['Health','Thirst','Hunger','Shelter durability'],loc='lower left')
ax1.set_xlabel('Day',fontsize=15)
ax1.set_ylabel('Value',fontsize=15)

ax2.grid(color='tab:grey',linestyle=':',linewidth=0.5)
ax2.plot(x,medkit_quantity,color='tab:red')
ax2.plot(x,water_quantity,color='tab:blue')
ax2.plot(x,food_quantity,color='tab:orange')
ax2.plot(x,material_quantity,color='green')
ax2.set_xticks(np.linspace(1,9,9))
ax2.set_xlim([1,9])
ax2.set_ylim([-0.2,max(material_quantity)])
ax2.legend(['Medkit','Water','Food','Material'],loc='best')
ax2.set_xlabel('Day',fontsize=15)
ax2.set_ylabel('Quantity',fontsize=15)
f.suptitle('Evolution of your gaming data',x=0.5,y=0.92,fontsize=18)
mp.show()
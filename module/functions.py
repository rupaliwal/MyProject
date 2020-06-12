import string

import random


# Making List for Animal Type and Animal Color.
animal = ['dog','cat','fish','Dog', 'Cat','Fish']


def animal_type(input_one):
    
    output = False
    
    if input_one in animal:
        output = True
    else:
        output = False
        
    return output

color = ['black','brown','gray', 'white','red','blue','yellow','orange','gold','Black',
         'Brown','Gray', 'White','Red','Blue','Yellow','Orange','Gold']


# Check Animal Color
def animal_col(input_two):
    
    output = False
    
    if input_two in color:
        output = True
    else:
        print("Please choose between black, brown, gray, white, red, blue, yellow, orange, or gold!")
        
    return output


# Makes Lists for DOG
dog_black = ['Ash', 'Bean','Bear', 'Black Beauty', 'BlackBerry', 'Cola', 'Boba']
dog_brown = ['Coco','Cookie','Honey','Chestnut','Acorn','Brownie']
dog_gray = ['Stormy','Astra', 'Ash','Coal','Dusty','Earl Gray','Stone','Stoney','Rocky']
dog_white = ['Cloud','Diamond','Icy','Misty', 'Iris','Cotton','Coconut','Dove','Milky']
dog_red = ['Autumn','Apple', 'Rusty','Brick','Copper','Scarlet','Rose','Cherry']
dog_blue = ['Navy','Blueberry','Azure','Sky','Teal','Winter']
dog_yellow = ['Lemon','Sunshine','Popcorn','Butter','Poppy','Nugget','Summer','Buttercup']
dog_orange = ['Fire','Apricot','Cheddar','Clementine','Maple']
dog_gold = ['Butter','Goldie','Butterscotch','Corona','Sandy','Caramel']

# Makes Lists for CAT
cat_black = ["Shadow", "Pepper", "Smokey", 'Midnight', 'Inky', 'Sesame']
cat_brown = ['Mocha', 'Snickers', 'Teddy',"Truffles", "Woody","Whiskey", "Chai", "Cinnamon"]
cat_gray = ['Comet','Dusty','Moon','Pebbles','Silvy','Thunder']
cat_white = ['Angel','Casper', 'Lily','Ivory','Marshmallow','Vanilla','Snowflake','Crystal']
cat_red = ['Rose','Crimson','Scarlett',"Ruby","Paprika", "Chili"]
cat_blue = ['Bay',"Bluebell","Aqua","Blueberry","Celestial", "Bubbles","Blue Star"]
cat_yellow = ["Banana", 'Winnie',"Daisy","Sunflower","Honey",'Canary',"Daffodil", "Macaroni"]
cat_orange = ['Pumpkin','Tiger','Dorito','Saffron',"Cheeto","Simba", "Ed Sheeran","Sweet Potato", "Fanta"]
cat_gold = ["Coin",'Goldie','Canoli','Precious',"Richie Rich","Nugget", "Flame"]

# Makes Lists for FISH
fish_black = ["Batman", "Cruella De Vil", "Raven","Midnight", "Sable", "Boba"]
fish_brown = ["Woody", "Maui (from Moana)", "Bruno", "Charlie Brown", "Dunkin"]
fish_gray = ["Moon", "Squidward", "Eeyore", "Ash/Ashley", "Pebbles", "Rocky"]
fish_white = ["Crystal","Elsa", "Donald Duck", "Olaf", "Snow White", "Bianca" ]
fish_red = ["Minnie", "Mickey","Crimson", "Patrick (Spongebob)", 
            "Mr. Krabs (Spongebob)","Brick", "Cerise"]
fish_blue = ["Bubbles","Blue","Dory","Aqua","Azure","Sky","Superman","Elsa","Hydra", 
             "Princess Jasmine", "Cinderella"]
fish_yellow = ["Bumblebee", "Flounder (Disney)", "Spongebob", "Amber", "Light", "Daisy", "Blossom"]
fish_orange = ["Nemo","Ariel", "Darwin (Disney- Amazing World of Gumball)", 
               "Mrs Puff (Spongebob)", "Goofy (Disney)", "Pluto (Disney)"]
fish_gold = ["Goldie", "Jewel", "Gold", "Penny", "Cleo (from Pinocchio)", "Rapunzel"]


# For Selecting Random Name for dog based on color.
def check_dog(type_animal, col_animal):
    
    if type_animal in ["Dog","dog"] and col_animal in ["Black","black"]:
        msg = random.choice(dog_black)
        print("A possible name could be "+ msg)
    elif type_animal in ["Dog","dog"] and col_animal in ["Brown","brown"]:
        msg = random.choice(dog_brown)
        print("A possible name could be "+ msg)
    elif type_animal in ["Dog","dog"] and col_animal in ["Gray","gray"]:
        msg = random.choice(dog_gray)
        print("A possible name could be "+ msg)    
    elif type_animal in ["Dog","dog"] and col_animal in ["White","white"]:
        msg = random.choice(dog_white)
        print("A possible name could be "+ msg)   
    elif type_animal in ["Dog","dog"] and col_animal in ["Red","red"]:
        msg = random.choice(dog_red)
        print("A possible name could be "+ msg)
    elif type_animal in ["Dog","dog"] and col_animal in ["Blue","blue"]:
        msg = random.choice(dog_blue)
        print("A possible name could be "+ msg)  
    elif type_animal in ["Dog","dog"] and col_animal in ["Yellow","yellow"]:
        msg = random.choice(dog_yellow)
        print("A possible name could be "+ msg)     
    elif type_animal in ["Dog","dog"] and col_animal in ["Orange","orange"]:
        msg = random.choice(dog_orange)
        print("A possible name could be "+ msg)    
    elif type_animal in ["Dog","dog"] and col_animal in ["Gold","gold"]:
        msg = random.choice(dog_gold)
        print("A possible name could be "+ msg)

# For Selecting Random Name for cat based on color.
def check_cat(type_animal, col_animal):
    
    if type_animal in ["Cat","cat"] and col_animal in ["Black","black"]:
        msg = random.choice(cat_black)
        print("A possible name could be "+ msg)
    elif type_animal in ["Cat","cat"] and col_animal in ["Brown","brown"]:
        msg = random.choice(cat_brown)
        print("A possible name could be "+ msg)
    elif type_animal in ["Cat","cat"] and col_animal in ["Gray","gray"]:
        msg = random.choice(cat_gray)
        print("A possible name could be "+ msg)    
    elif type_animal in ["Cat","cat"] and col_animal in ["White","white"]:
        msg = random.choice(cat_white)
        print("A possible name could be "+ msg)   
    elif type_animal in ["Cat","cat"] and col_animal in ["Red","red"]:
        msg = random.choice(cat_red)
        print("A possible name could be "+ msg)
    elif type_animal in ["Cat","cat"] and col_animal in ["Blue","blue"]:
        msg = random.choice(cat_blue)
        print("A possible name could be "+ msg)    
    elif type_animal in ["Cat","cat"] and col_animal in ["Yellow","yellow"]:
        msg = random.choice(cat_yellow)
        print("A possible name could be "+ msg)    
    elif type_animal in ["Cat","cat"] and col_animal in ["Orange","orange"]:
        msg = random.choice(cat_orange)
        print("A possible name could be "+ msg)    
    elif type_animal in ["Cat","cat"] and col_animal in ["Gold","gold"]:
        msg = random.choice(cat_gold)
        print("A possible name could be "+ msg)
        
# For Selecting Random Name for fish based on color.
def check_fish(type_animal, col_animal):
    
    if type_animal in ["Fish",'fish'] and col_animal in ["Black","black"]:
        msg = random.choice(fish_black)
        print("A possible name could be "+ msg)
    elif type_animal in ["Fish",'fish'] and col_animal in ["Brown","brown"]:
        msg = random.choice(fish_brown)
        print("A possible name could be "+ msg)
    elif type_animal in ["Fish",'fish'] and col_animal in ["Gray","gray"]:
        msg = random.choice(fish_gray)
        print("A possible name could be "+ msg)  
    elif type_animal in ["Fish",'fish'] and col_animal in ["White","white"]:
        msg = random.choice(fish_white)
        print("A possible name could be "+ msg) 
    elif type_animal in ["Fish",'fish'] and col_animal in ["Red","red"]:
        msg = random.choice(fish_red)
        print("A possible name could be "+ msg)
    elif type_animal in ["Fish",'fish'] and col_animal in ["Blue","blue"]:
        msg = random.choice(fish_blue)
        print("A possible name could be "+ msg)     
    elif type_animal in ["Fish",'fish'] and col_animal in ["Yellow","yellow"]:
        msg = random.choice(fish_yellow)
        print("A possible name could be "+ msg)     
    elif type_animal in ["Fish",'fish'] and col_animal in ["Orange","orange"]:
        msg = random.choice(fish_orange)
        print("A possible name could be "+ msg)    
    elif type_animal in ["Fish",'fish'] and col_animal in ["Gold","gold"]:
        msg = random.choice(fish_gold)
        print("A possible name could be "+ msg)

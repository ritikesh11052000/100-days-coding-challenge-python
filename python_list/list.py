

list = ["Afghanistan", "Albania", "Algeria", "Andorra",
        "Angola", "Antigua and Barbuda", "Argentina",
        "Armenia", "Australia", "Austria", "Azerbaijan",
        "Bahamas", "Bahrain", "Bangladesh", "Barbados",
        "Belarus", "Belgium", "Belize", "Benin", "Bhutan",
        "Bolivia", "Bosnia and Herzegovina", "Botswana",
        "Brazil", "Brunei", "Bulgaria", "Burkina Faso",
        "Burundi", "Cabo Verde", "Cambodia", "Cameroon",
        "Canada", "Central African Republic", "Chad",
        "Chile", "China", "Colombia", "Comoros", "Congo",
        "Democratic Republic of the", "Congo",
       ]

anime_list = [
    "Naruto",
    "One Piece",
    "Dragon Ball Z",
    "Death Note",
    "Attack on Titan",
    "My Hero Academia",
    "Fullmetal Alchemist: Brotherhood",
    "One Punch Man",
    "Tokyo Ghoul",
    "Sword Art Online",
    "Hunter x Hunter",
    "Bleach",
    "Fairy Tail",
    "Demon Slayer",
    "Steins;Gate",
    "Code Geass",
    "Cowboy Bebop",
    "Neon Genesis Evangelion",
    "Black Clover",
    "Dragon Ball",
    "JoJo's Bizarre Adventure",
    "The Seven Deadly Sins",
    "Naruto Shippuden",
    "Re:Zero",
    "Mob Psycho 100",
    "The Promised Neverland",
    "Overlord",
    "Gurren Lagann",
    "Erased",
    "Haikyuu!!",
    "Attack on Titan: Junior High",
    "Black Butler",
    "Death Parade",
    "Durarara!!",
    "Noragami",
    "No Game No Life",
    "Assassination Classroom",
    "Akame ga Kill!",
    "Fate/stay night",
    "Blue Exorcist",
    "Parasyte",
    "Soul Eater",
    "Toradora!",
    "High School DxD",
    "The Rising of the Shield Hero",
    "Fruits Basket",
    "Danganronpa",
    "Hellsing",
    "Magi: The Labyrinth of Magic"
]

# print(anime_list,list)

length = len(list)

print(f"{length}")

print(f"{list[4]}")




# list using random module: - 

names = ["sanji","nami","luffy","zoro","ussap","robin","choper","jinbme","franky","Brook","zeus"]

# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random

num_item = len(names)

random_choice = random.randint(0,num_item -1)

p_w_pay = names[random_choice]
print(f"{p_w_pay} is going to buy the meal today!")


#print("Hello from lesson 5")
#Recap
#Task 1a
#food = ["Ice cream", "Burger", "Vanilla Cake", "Spaghetti", "Oreo Cheesecake"]

#Task 1b
#food.pop(2)

#Task 1c
#food.append("Seaweed")

#Task 1d
#for i in range(len(food)):
#    print(food[i])

#Not a recap
#Task 1 (EDITED INTO tASK 2)
#import random
#luckyNum = []
#random_num = 0
#while len(luckyNum) < 100:
#    random_num = random.randint(1, 1000)
#    if random_num not in luckyNum:
#        luckyNum.append(random_num)
#print(luckyNum)
#print(len(luckyNum))

#Task 3:
#import random
#mathScores = []
#score = 0
#lowest = 0
#top = 0
#average = 0

#while len(mathScores) < 100:
#    score = random.randint(0, 100)
#    mathScores.append(score)

#print(mathScores)
#print(len(mathScores))
#lowest = min(mathScores)
#top = max(mathScores)
#average = sum(mathScores)/len(mathScores)

#print(lowest)
#print(top)
#print(average)

#Task 4:
#shortest = 0
#namelist = ["Olivia", "Liam", "Emma", "Noah", "Ava", "Ethan",
#            "Sophia", "Lucas", "Mia", "Aiden"
#            ]
#heightlist = [160, 165, 158, 170, 162, 168, 159, 172, 164, 166]

#shortest = namelist[heightlist.index(max(heightlist))]
#tallest = namelist[heightlist.index(min(heightlist))]

#print(shortest)
#print(tallest)

#Task 5:
import random
pokemon1 = ""
pokemonIndex1 = 0
pokemonPower1 = 0
pokemon2 = ""
pokemonIndex2 = 0
pokemonPower2 = 0
winner = ""
pokemons = [
    "Pikachu", "Charizard", "Bulbasaur", "Squirtle",
    "Jigglypuff", "Meowth", "Psyduck", "Eevee", "Snorlax",
    "Mewtwo", "Lapras", "Gengar", "Dragonite", "Machamp",
    "Arcanine", "Alakazam", "Gyarados", "Vaporeon", "Scyther",
    "Electabuzz"
]

powers = [
    55, 84, 49, 48, 45,
    45, 52, 55, 110, 110,
    85, 65, 134, 130, 110,
    50, 125, 65, 110, 83 
]

pokemon1 = random.choice(pokemons)
pokemonIndex1 = pokemon1.index(pokemon1)
pokemonPower1 = powers[pokemonIndex1]

pokemon2 = random.choice(pokemons)
while pokemon1 == pokemon2:
    pokemon2 = random.choice(pokemons)
pokemonIndex2 = pokemon2.index(pokemon2)
pokemonPower2 = powers[pokemonIndex2]

if pokemonPower1 < pokemonPower2:
    winner = pokemon2
else:
    winner = pokemon1

print(f"{pokemon1} verus {pokemon2}. {winner} wins!")

#powers[pokemonIndex1]
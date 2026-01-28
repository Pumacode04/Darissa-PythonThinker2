#print("Hello from lesson 4")
# Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune)
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

#Task 1b :
#planets[3] = "RedCircle"
#print(planets[3])

#Task 1c :
#planets.append("Pluto")
#planets.insert(3, "LalaLand")

#task 1d :
#planets.remove("Jupiter")
#OR
#planets.pop(5) #5 coz of LalaLand

#print(planets)

#task 2 :
#for i in range(len(planets)):
#    if planets[i] == "Earth":
#        print(planets[i] + " : this is my home!")
#    elif planets[i] == "RedCircle":
#        print(planets[i] + " : I conquered it!")
#    elif planets[i] == "LalaLand":
#        print(planets[i] + " : is in your dreams.")
#    else:
#        print(planets[i])

#task 3 :
#crazyTravelList = []
#country = ""

#while country != "end":
#    country = input("What country you want to go. ")
#    if country == "end":
#        break
#    crazyTravelList.append(country)
#for i in range(len(crazyTravelList)):
#    print("I would like to visit : " + (crazyTravelList[i]))

#task 4a :
menu = []
food = ""
custo = ""
stock = 0

while food != "end":
    food = input("what you want on your food menu.")
    if food == "end":
        break
    menu.append(food)

print(menu)
#task 4b:
custo = "hey what you like to eat."
for i in range(len(menu)):
    custo = input("hey what you like to eat.")
    if custo == menu[i]:
        print("yes, we have that")
        stock += 1
        break
    else:
        break
if stock == 0:
    print("go next door see")

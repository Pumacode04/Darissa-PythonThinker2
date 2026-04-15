#print("Hello from lesson 12")
#Task 1:

# def print_title():
#   print("""
#     ██████╗  ██████╗  ██████╗ ███████╗  ██████╗ ██╗   ██╗███████╗███████╗████████╗
#    ██╔════╝ ██╔═══██╗ ██╔══██╗██╔════╝ ██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝
#    ██║      ██║   ██║ ██║  ██║█████╗   ██║   ██║██║   ██║█████╗  ███████╗   ██║   
#    ██║      ██║   ██║ ██║  ██║██╔══╝   ██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║   
#    ╚██████╗ ╚██████╔╝ ██████╔╝███████╗ ╚██████╔╝╚██████╔╝███████╗███████║   ██║   
#     ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   
# """)

# def introduction():
#     print("Introduction:")
#     print("Wecome, adventurer!")
#     print("This is a mini text game where you choose what to do next.")

# def rules():
#    print("Rules:")
#    print("1) Type the number of your choice and press 'Enter'.")
#    print("2) Read carefully -- some choices may end the game.")
#    print("3) Have fun and don't panic if you make a mistake!")

# def show_menu():
#    print("Menu:")
#    print("1) Start Game")
#    print("2) Instructions")
#    print("3) Quit")

# def separator():
#    print("============================================")

# def game_intro():
#    print_title()
#    introduction()
#    separator()
#    rules()
#    separator()
#    show_menu()
#    separator()

# game_intro()

#Task 2:
def notice():
    print("***** QUEST BOARD NOTICE *****")

def quest_header(name, reward):
    print(f"Quest: {name}")
    print(f"Reward: {reward}")

def details(location, danger_level):
    print(f"Location: {location}")
    print(f"Danger Level: {danger_level}")
    if danger_level == "low":
      print("Advice: Just watch out.")
    elif danger_level == "medium":
        print("Advice: stay alert.")
    else:
        print("Advice: Try to stay alive.")
def seperator():
    print("=============================================")

def space():
    print("")

def board(name, reward, location, danger_level):
    notice()
    quest_header(name, reward)
    seperator()
    details(location, danger_level)

board("Cross the broken bridge", "Access to other quests", "station A", "low")
space()
board("The gas is posionous, reach an underground station", "Survival", "Station C", "Medium")

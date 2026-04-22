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
# def notice():
#     print("***** QUEST BOARD NOTICE *****")

# def quest_header(name, reward):
#     print(f"Quest: {name}")
#     print(f"Reward: {reward}")

# def details(location, danger_level):
#     print(f"Location: {location}")
#     print(f"Danger Level: {danger_level}")
#     if danger_level == "low":
#       print("Advice: Just watch out.")
#     elif danger_level == "medium":
#         print("Advice: stay alert.")
#     else:
#         print("Advice: Try to stay alive.")
# def seperator():
#     print("=============================================")

# def space():
#     print("")

# def board(name, reward, location, danger_level):
#     notice()
#     quest_header(name, reward)
#     seperator()
#     details(location, danger_level)
#     space()

# board("Cross the broken bridge", "Access to other quests", "station A", "low")
# board("The gas is posionous, reach an underground station", "Survival", "Station C", "medium")

#Task 3:
# import random
# monster_name = "Cave Slime King"
# monster_hp = 25
# danger_level = "medium"
# reward = 100
 
# print("=== BOSS FIGHT ===")
# print(f"Enemy: {monster_name}")
# print(f"Monster HP (start): {monster_hp}")

# def roll_dice(sides):
#     return random.randint(1, sides)

# attack_roll = roll_dice(20)
# print(f"Attack roll: {attack_roll}")


# def calculate_damage(attack_roll):
#     bonus_damage = random.randint(1,5)
#     final_damage = attack_roll + bonus_damage
#     if attack_roll >= 18:
#         final_damage = final_damage * 2
#     return final_damage

# damage = calculate_damage(attack_roll)
# print(f"Damage dealt: {damage}")

# def apply_damage(current_hp, damage):
#     current_hp -= damage
#     if current_hp < 0:
#         current_hp = 0
#     return current_hp

# monster_hp = apply_damage(monster_hp, damage)
# print(f"Monster HP (after): {monster_hp}")

# def calculate_reward(base_gold, danger_level):
#     if danger_level.lower() == "low":
#         pass
#     elif danger_level.lower() == "medium":
#         base_gold *= 1.5
#     elif danger_level.lower == "high":
#         base_gold *= 2
#     else:
#         base_gold *= 1.2
#     return base_gold
        
# gold_reward = calculate_reward(reward, danger_level)
# #print(f"Gold Earned: {gold_reward}")

# def get_battle_message(monster_name, monster_hp, gold_reward):
#     if monster_hp == 0:
#         print(f"You have defeated {monster_name}.")
#         print(f"Gold Earned: {gold_reward}")
#     else:
#         print(f"{monster_name} is still alive!")
#         print(f"Monster HP (remaining) : {monster_hp}")

# get_battle_message(monster_name, monster_hp, gold_reward)

#Task 3 modified:
# import random
# monster_name = "Cave Slime King"
# monster_hp = 25
# danger_level = "medium"
# reward = 100

# print("=== BOSS FIGHT ===")
# print(f"Enemy: {monster_name}")
# print(f"Monster HP (start): {monster_hp}")

# def roll_dice(sides):
#     return random.randint(1, sides)

# def calculate_damage(attack_roll):
#     bonus_damage = random.randint(1,5)
#     final_damage = attack_roll + bonus_damage
#     if attack_roll >= 18:
#         final_damage = final_damage * 2
#     return final_damage

# def apply_damage(current_hp, damage):
#     current_hp -= damage
#     if current_hp < 0:
#         current_hp = 0
#     return current_hp

# def calculate_reward(base_gold, danger_level):
#     if danger_level.lower() == "low":
#         pass
#     elif danger_level.lower() == "medium":
#         base_gold *= 1.5
#     elif danger_level.lower == "high":
#         base_gold *= 2
#     else:
#         base_gold *= 1.2
#     return base_gold
        
# def get_battle_message(monster_name, monster_hp, gold_reward):
#     if monster_hp == 0:
#         print(f"You have defeated {monster_name}.")
#         print(f"Gold Earned: {gold_reward}")
#     else:
#         print(f"{monster_name} is still alive!")
#         print(f"Monster HP (remaining) : {monster_hp}")

# gold_reward = calculate_reward(reward, danger_level)

# turn = 1

# while monster_hp > 0:
#     print(f"Round --- {turn} ---")
#     attack_roll = roll_dice(20)
#     print(f"Attack roll: {attack_roll}")

#     damage = calculate_damage(attack_roll)
#     print(f"Damage dealt: {damage}")

#     monster_hp = apply_damage(monster_hp, damage)
#     get_battle_message(monster_name, monster_hp, gold_reward)

#     turn += 1

#Task 3 modified again:
import random
def start_boss_fight(monster_name, monster_hp, danger_level, reward):
    print("=== BOSS FIGHT ===")
    print(f"Enemy: {monster_name}")
    print(f"Monster HP (start): {monster_hp}")

    def roll_dice(sides):
        return random.randint(1, sides)

    def calculate_damage(attack_roll):
        bonus_damage = random.randint(1,5)
        final_damage = attack_roll + bonus_damage
        if attack_roll >= 18:
            final_damage = final_damage * 2
        return final_damage

    def apply_damage(current_hp, damage):
        current_hp -= damage
        if current_hp < 0:
            current_hp = 0
        return current_hp

    def calculate_reward(base_gold, danger_level):
        if danger_level.lower() == "low":
            pass
        elif danger_level.lower() == "medium":
            base_gold *= 1.5
        elif danger_level.lower == "high":
            base_gold *= 2
        else:
            base_gold *= 1.2
        return base_gold
        
    def get_battle_message(monster_name, monster_hp, gold_reward):
        if monster_hp == 0:
            print(f"You have defeated {monster_name}.")
            print(f"Gold Earned: {gold_reward}")
        else:
            print(f"{monster_name} is still alive!")
            print(f"Monster HP (remaining) : {monster_hp}")

    gold_reward = calculate_reward(reward, danger_level)

    turn = 1

    while monster_hp > 0:
        print(f"Round --- {turn} ---")
        attack_roll = roll_dice(20)
        print(f"Attack roll: {attack_roll}")

        damage = calculate_damage(attack_roll)
        print(f"Damage dealt: {damage}")

        monster_hp = apply_damage(monster_hp, damage)
        get_battle_message(monster_name, monster_hp, gold_reward)

        turn += 1
        print("")

start_boss_fight("Cave Slime King", 25, "Medium", 100)
start_boss_fight("Rubber Ducky", 150, "High", 250)
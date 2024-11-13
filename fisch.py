from math import sqrt

while True:
    print("Are you level 500 or below?")
    print("Answer 1 for level 500 and 2 for below level 500.")
    choice = input("")
    if choice == "1":
        print("How much bonus xp do you have?")
        bonus_xp = input("")
        if bonus_xp.isdigit() == True:
            bonus_xp = int(bonus_xp)
            if bonus_xp < 0:
                print("Write a real number above 0.")
                continue
            else:
                level = sqrt((2*(bonus_xp + 23750000))/190)
                print(f"You have a total of {bonus_xp + 23750000} xp.")
                print(f"This makes your true level {int(level)}!")
                print(f"Answer either 1 to restart or 2 to see how much xp is needed to reach a specific level.")
                choice = input("")
                if choice == "1":
                    continue
                elif choice == "2":
                    print("What level do you want to reach?")
                    level_goal = input("")
                    if level_goal.isdigit() == True:
                        level_goal = int(level_goal)
                        if level_goal <= int(level):
                            print(f"Write a real number for a level thats hbigher than your true level ({int(level)})")
                            continue
                        elif level_goal > int(level):
                            xp_goal = (190 * level_goal * level_goal)/2
                            print(f"You need {xp_goal - bonus_xp - 23750000} xp more to reach lvl {level_goal}.")
                        else:
                            print("Error.")
                            continue
                    else:
                        print(f"Write a real number for a level thats higher than your true level ({int(level)}).")
                        continue
                else:
                    "Pick either 1 or 2 next time"
                    continue
        else:
            print("Write a real number above 0.")
            continue

    elif choice == "2":
        print("What level are you?")
        level = input("")
        if level.isdigit() == True:
            level = int(level)
            if level < 0:
                print("Write a real number above 0.")
                continue
            else:
                xp = (190 * level * level)/2
                print(f"You have a total of {xp} xp, to reach level 500 you need 23 750 000 xp.")
                print(f"You are {int((xp/23750000)*100)}% there.")
                continue
        else:
            print("Write a real number above 0.")
            continue
    else:
        print("Write either 1 or 2.")
        continue
    



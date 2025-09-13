# decision_tree.py
# Life Decision Simulator: guiding you through the smallest choices
# with the importance of a nuclear treaty negotiation.

print("🌍 Welcome, human. Today, your destiny hinges upon...")
print("...the most trivial yet earth-shattering decision of your life.")
print("Brace yourself. History books will remember this moment.\n")

# Question 1
breakfast = input("Did you eat breakfast today? (yes/no): ").strip().lower()

if breakfast == "yes":
    # Question 2
    drink = input("Did you drink coffee or tea? (coffee/tea/none): ").strip().lower()
    
    if drink == "coffee":
        # Question 3
        sugar = input("Did you add sugar? (yes/no): ").strip().lower()
        if sugar == "yes":
            print("\n🔥 Congratulations. Your glucose-fueled brain will invent time travel by 3pm.")
        else:
            print("\n☕ Your bitter resolve inspires nations. Sadly, you will also forget your Netflix password forever.")
    
    elif drink == "tea":
        # Question 4
        fancy = input("Was it herbal tea? (yes/no): ").strip().lower()
        if fancy == "yes":
            print("\n🌿 Herbal wisdom flows through you. Unfortunately, you’ll also start speaking only in riddles.")
        else:
            print("\n🍵 A true leaf warrior. The Queen of England will knight you in a surprise ceremony.")
    
    else:  # none
        # Question 5
        water = input("Did you at least drink water? (yes/no): ").strip().lower()
        if water == "yes":
            print("\n💧 Hydration complete. You ascend to the title of Moisture Lord, ruler of all humidifiers.")
        else:
            print("\n🚫 No drinks at all? Bold. You spontaneously combust in a burst of dramatic irony.")
            
else:  # no breakfast
    # Question 2
    mood = input("Are you currently hangry? (yes/no): ").strip().lower()
    
    if mood == "yes":
        # Question 3
        snack = input("Do you plan to eat a snack soon? (yes/no): ").strip().lower()
        if snack == "yes":
            print("\n🥨 Crisis averted. You prevent World War III with a single granola bar.")
        else:
            print("\n💥 Without a snack, your rage destabilizes the economy. Thanks a lot.")
    
    else:  # not hangry
        # Question 4
        confidence = input("Are you confident you can make it to lunch? (yes/no): ").strip().lower()
        if confidence == "yes" and not mood == "yes":
            print("\n😌 Your inner peace inspires humanity. Someone writes a Broadway musical about your stomach growls.")
        else:
            # Question 5
            backup = input("Do you at least have emergency gummy bears? (yes/no): ").strip().lower()
            if backup == "yes":
                print("\n🍬 Victory is yours. You ascend Mount Olympus fueled entirely by gummy bears.")
            else:
                print("\n📉 No plan. No snacks. No hope. Your legacy is a cautionary tale in nutrition textbooks.")

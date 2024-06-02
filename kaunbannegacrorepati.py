questions = [
    ["A. what is the capital city of Nepal?", "kathmandu", "dhading", "chitwan", "pokhara", 1],
    ["B. where is Mt. Everest located?", "kathmandu", "dhading", "chitwan", "solukhambhu", 4],
    ["C. how many people live in Nepal?", "3 cr", "4cr", "5cr", "6cr", 1],
    ["D. who is the prime minister of Nepal?"]
]
levels = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 50000, 100000]

for i in range(len(questions)):
    current_question = questions[i]
    print(f"Question for Rs.{levels[i]}")
    print(current_question[0])  # Print the question
    print()
    print(f"1.{current_question[1]}    2.{current_question[2]}")
    print(f"3.{current_question[3]}    4.{current_question[4]}")

    reply = int(input("Enter your number (1-4): "))

    if i == 3:  # Check if it's the last question
        correct_answer = input("Enter the correct answer: ")
        if correct_answer.lower() == "kp sharma oli":
            print(f"Correct answer! You have won Rs.{levels[i]}")
            print(f"You take your money: Rs.{levels[i]}")
        else:
            print("Wrong answer!")
    elif reply == current_question[-1]:
        print(f"Correct answer! You have won Rs.{levels[i]}")
        if i == 2:  # Check if it's the last but one question
            money = 100000
        else:
            money = levels[i]

        print(f"You take your money: Rs.{money}")
    else:
        print("Wrong answer!")
        break
    print(f"your money deducted to Rs 1000")

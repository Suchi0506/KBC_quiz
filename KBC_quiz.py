import random
import sys

guess = ''
score = 0
question_num = 0
lifeline_choice = {1: "50_50", 2: "Double dip", 3: "Flip the question"}
amount_won = 0
lifelines_used = {'50_50': False, 'Double dip': False, 'Flip the question': False}
total_lifelines_used = 0

print("********************************")
print()
print("Welcome to Kaun Banega Crorepati")
print("********************************")
print (str(input("Enter your name:")))
print(".................................................")
questions = ["The International Literacy Day is observed on",
             "The language of Lakshadweep, a Union Territory of India, is:",
             "In which group of places the Kumbha Mela is held every twelve years?",
             "Bahubali festival is related to:",
             "Which day is observed as the World Standards  Day?",
             "Which is the largest planet in the solar system?",
             "Which of the following was the theme of the World Red Cross and Red Crescent Day?",
             "September 27 is celebrated every year as:",
             "Who is the author of 'Manas Ka-Hans'?",
             "Who is the author of the epic 'Meghdoot?",
             "Good Friday is observed to commemorate the event of:",
             "Who is the author of the book 'Amrit Ki Ore'?",
             "Which of the following is observed as Sports Day every year?",
             "World Health Day is observed on:",
             "Pongal is a popular festival of which state?"
             ]

options = [["A. Sept 8", "B. Sept 28", "C. Nov 22", "D. May 8"],
           ["A. Tamil", "B. Hindi", "C. Malayalam", "D. Telugu"],
           ["A. Ujjain, Puri, Prayag, Haridwar", "B. Prayag, Haridwar, Ujjain, Nasik",
            "C. Rameshwaram, Puri, Badrinath, Dwarika", "D. Chittakoot, Ujjain, Prayag, Haridwar"],
           ["A. Islam", "B. Buddhism", "C. Hinduism", "D. Jainism"],
           ["A. June 26", "B. Oct 14", "C. Nov 15", "D. Dec 2"],
           ["A. Jupiter", "B. Saturn", "C. Uranus", "D. Neptune"],
           ["A. Dignity for all - focus on women", "B. Dignity for all - focus on Children",
            "C. Focus on health for all", "D. Nourishment for all-focus on children"],
           ["A. Teachers Day", "B. National Integration Day", "C. World Tourism Day", "D. Interntional Literacy Day"],
           ["A. Khushwant Singh", "B. Prem Chand", "C.Jayashankar Prasad", "D. Amrit Lal Nagar"],
           ["A. Vishakadatta", "B. Valmiki", "C. Banabhatta", "D. Kalidas"],
           ["A. birth of Jesus Christ", "B. birth of' St. Peter", "C. crucification 'of Jesus Christ",
            "D. rebirth of Jesus Christ"],
           ["A. 22nd April", "B. 26th July", "C. 29th August", "D. 2nd October"],
           ["A. Apr 7", "B. Mar 6", "C. Mar I5", "D. Apr 28"],
           ["A. Karnataka", "B. Kerela", "C. Tamil Nadu", "D. Andhra Pradesh"]
           ]
remaining_options = []
answers = [["A. Sept 8"], ["C. Malayalam"], ["B. Prayag, Haridwar, Ujjain, Nasik"],
           ["D. Jainism"], ["B. Oct 14"], ["A. Jupiter"], ["C. Focus on health for all"],
           ["C. World Tourism Day"], ["D. Amrit Lal Nagar"], ["D. Kalidas"],
           ["C. crucification of Jesus Christ"], ["B. Narendra Mohan"], ["C. 29th August"],
           ["A. Apr 7"], ["C. Tamil Nadu"]
           ]
amount = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000,
          320000, 640000, 1250000, 2500000, 500000, "1crore"]

flip_question = ["Name of the first Atomic Submarine of India?",
                 "What is the name of first British to visit India?",
                 "Name of the first election commissioner of India?"]
flip_option = [["A. I.N.S Chakra", "B. R.N. Shukla", "C. V.R. Gill", "D. D.B. Mahawar"],
               ["A. Hawkins", "B. Norway", "C. Devid", "D. George Bush"],
               ["A. Sukumar Sen", "B.RN Shukla", "C. V.R. Gill", "D. D.B. Mahawar"]
               ]
flip_answer = [["A. I.N.S Chakra"], ["A. Hawkins"], ["A. Sukumar Sen"]]

for question_num in range(len(questions)):
    question = questions[question_num]
    print(f"Question No. {question_num + 1}: {question}")
    print("_________________________________________________________________")

    options_for_question = options[question_num]
    correct_answer = answers[question_num][0]

    for option in options_for_question:
        print(option)

    while True:
        guess = input("Enter your answer choice (A, B , C, D) or use lifeline 'L' or Enter 'Q' to Quit:")
        # checking if the entered value is correct
        if guess.upper() in ("A", "B", "C", "D", "L", "Q"):
            break
        # checking if the entered value is not correct
        else:
            print("Please enter a valid choice")
            continue

    if guess.upper() in ("A", "B", "C", "D"):
        if guess.upper() == correct_answer[0]:
            print(f"----------Congratulations!! You gave correct answer for Question No. {question_num}----------")
            score = score + 1
            print("Score:", score)
            amount_won = amount[question_num]
            print(f"----------Your total amount won is: {amount_won}---------")
            print(f"---------------------------------------------------------")
            print(f"----------Let's move to the next question----------------")
            print(f"---------------------------------------------------------")
            continue
        else:
            print("Incorrect")
            print("Score:", score)
            print("Amount won:", amount_won)
            break

    elif guess.upper() == "Q":
        print("You have chosen to quit the game")
        print("Score:", score)
        print("Amount won:", amount_won)
        break

    elif guess.upper() == "L":
        if total_lifelines_used >= 3:
            print("You don't have any lifeline left.")

            while True:
                guess = input("Enter your answer choice (A, B , C, D) or Enter 'Q' to Quit:")
                # checking if the entered value is correct
                if guess.upper() in ("A", "B", "C", "D", "Q"):
                    break
                # checking if the entered value is not correct
                else:
                    print("Please enter a valid choice")
                    continue

            if guess.upper() in ("A", "B", "C", "D"):
                if guess.upper() == correct_answer[0]:
                    print(f"----------Congratulations!! You gave correct answer for Question No. {question_num}----------")
                    score = score + 1
                    print("Score:", score)
                    amount_won = amount[question_num]
                    print(f"----------Your total amount won is: {amount_won}---------")
                    print(f"---------------------------------------------------------")
                    print(f"----------Let's move to the next question----------------")
                    print(f"---------------------------------------------------------")
                    continue
                else:
                    print("Incorrect")
                    print("You are out of the game")
                    print("Score:", score)
                    print("Amount won:", amount_won)
                    sys.exit()
                    

            elif guess.upper() in ("Q"):
                print("You have chosen to quit the game")
                print("Score:", score)
                if score == 5:
                    print("Total Amount won= 10000")
                elif score < 5:
                    print("Total Amount won= 0")
                elif score == 10:
                    print("Total Amount won= 32000")
                elif score < 10 and score > 5:
                    print("Total Amount won= 10000")
                elif score >= 10:
                    print("Total Amount won:", amount[question_num])

                else:
                    print("Game over!")
                    print("Score:", score)
                    print("Amount won:", amount_won)
                    break

        print("Lifeline options available are as follows:")
        remaining_options = []
        for value in lifeline_choice:
            if lifelines_used[lifeline_choice[value]] == False:
                print(value, lifeline_choice[value])
                remaining_options.append(value)
            else:
                continue

        while True:
            lifeline_opted = int(input(f"Please choose a lifeline from {remaining_options}"))
            if lifeline_opted in (1, 2, 3):
                break
            else:
                print("Please enter a valid choice")
                continue

        if lifeline_opted == 1 and lifelines_used['50_50'] == False:
            lifelines_used['50_50'] = True
            print("You have chosen 50-50 lifeline")
            print(f"Question No. {question_num + 1}: {question}")
            print("_________________________________________________________________")
            question_options = options[question_num]
            question_answer = answers[question_num][0]
            question_options.remove(question_answer)
            my_list = []
            my_list.append(question_answer)
            random_option = random.choice(question_options)
            my_list.append(random_option)
            my_list.sort()
            print("New Options after 50:50 are: ")
            print(my_list[0])
            print(my_list[1])
            total_lifelines_used = total_lifelines_used + 1

            while True:
                use_another_lifeline = (input("Do you wish to use another lifeline:(Y/N)"))
                if use_another_lifeline.upper() in ("Y", "N"):
                    break
                else:
                    print("Please enter a valid choice:")
                    continue

            if use_another_lifeline.upper() == 'N':
                remaining_5050_options = []
                for option in my_list:
                    remaining_5050_options.append(option[0])

                # print(f"Please enter a valid choice {remaining_5050_options}")

                guess = input(f"Enter your answer choice:")
                if guess.upper() == answers[question_num][0][0].upper():
                    print(f"----------Congratulations!! You gave correct answer for Question No. {question_num}----------")
                    score = score + 1
                    print("Score:", score)
                    amount_won = amount[question_num]
                    print(f"----------Your total amount won is: {amount_won}---------")
                    print(f"---------------------------------------------------------")
                    print(f"----------Let's move to the next question----------------")
                    print(f"---------------------------------------------------------")
                    continue
                else:
                    print("Incorrect")
                    print("You are out of the game")
                    print("Score:", score)
                    print("Amount won:", amount_won)
                    sys.exit()


            elif use_another_lifeline.upper() == 'Y':
                while True:
                    if total_lifelines_used < 3:
                        print("You have chosen Flip the question lifeline as you can not use Double Dip and 50_50 on the same question")
                        lifelines_used['Flip the question'] = True

                        random_index = random.randint(0, len(flip_question) - 1)
                        print("Display the question for flip lifeline:")
                        print(flip_question[random_index])
                        for option in flip_option[random_index]:
                            print(option)
                        total_lifelines_used += 1

                        while True:
                            use_another_lifeline = (input("Do you wish to use another lifeline:(Y/N)"))
                            if use_another_lifeline.upper() in ("Y", "N"):
                                break
                            else:
                                print("Please enter a valid choice")
                                continue

                        if use_another_lifeline.upper() == 'N':
                            guess = input("Enter your response (A,B,C,D)")
                            if guess.upper() == flip_answer[random_index][0][0].upper():
                                print(f"----------Congratulations!! You gave correct answer for Question No. {question_num}----------")
                                score = score + 1
                                print("Score:", score)
                                amount_won = amount[question_num]
                                print(f"----------Your total amount won is: {amount_won}---------")
                                print(f"---------------------------------------------------------")
                                print(f"----------Let's move to the next question----------------")
                                print(f"---------------------------------------------------------")
                                continue
                            else:
                                print("Incorrect")
                                print("You are out of the game")
                                print("Score:", score)
                                print("Amount won:", amount_won)
                                break


                        elif use_another_lifeline.upper() == 'Y':
                            print("You can only choose double dip lifeline")
                            total_lifelines_used = total_lifelines_used + 1
                            guess1 = input("Enter your first guess: (A,B,C,D)")
                            if guess1.upper() == flip_answer[random_index][0][0].upper():
                                print(f"----------Congratulations!! You gave correct answer for Question No. {question_num}----------")
                                score = score + 1
                                print("Score:", score)
                                amount_won = amount[question_num]
                                print(f"----------Your total amount won is: {amount_won}---------")
                                print(f"---------------------------------------------------------")
                                print(f"----------Let's move to the next question----------------")
                                print(f"---------------------------------------------------------")
                                continue
                            else:
                                print("Your first guess is wrong, try one more time")
                                for option in flip_option[random_index]:
                                    if option.upper().startswith(guess1.upper()):
                                        flip_option[random_index].remove(option)
                                        break
                                print("Remaining options:", flip_option[random_index])
                                guess2 = input("Enter your second guess:")
                                if guess2.upper() == flip_answer[random_index][0][0]:
                                    print(f"----------Congratulations!! You gave correct answer for Question No. {question_num}----------")
                                    score = score + 1
                                    print("Score:", score)
                                    amount_won = amount[question_num]
                                    print(f"----------Your total amount won is: {amount_won}---------")
                                    print(f"---------------------------------------------------------")
                                    print(f"----------Let's move to the next question----------------")
                                    print(f"---------------------------------------------------------")
                                    continue

                                else:
                                    print("Your second guess is also wrong")
                                    print("You are out of the game")
                                    print("Score:", score)
                                    print("Amount won:", amount_won)
                                    break
                    else:
                        print("You have already used all your lifelines")
                        while True:
                            guess = input(f"Enter your answer choice (A,B,C,D) or Enter 'Q' to Quit:")
                            if guess.upper() in ("A", "B", "C", "D", "Q"):
                                break
                            else:
                                print("Please enter a valid choice")
                                continue

                        if guess.upper() == answers[question_num][0][0].upper():
                            print(
                                f"----------Congratulations!! You gave correct answer for Question No. {question_num}----------")
                            score = score + 1
                            print("Score:", score)
                            amount_won = amount[question_num]
                            print(f"----------Your total amount won is: {amount_won}---------")
                            print(f"---------------------------------------------------------")
                            print(f"----------Let's move to the next question----------------")
                            print(f"---------------------------------------------------------")
                            continue
                        else:
                            print("Incorrect")
                            print("You are out of the game")
                            print("Score:", score)
                            print("Amount won:", amount_won)
                            break


        elif lifeline_opted == 2 and lifelines_used['Double dip'] == False:
            lifelines_used['Double dip'] = True
            print("You have chosen Double dip lifeline")
            total_lifelines_used += 1
            print(f"Question No. {question_num + 1}: {question}")
            print("_________________________________________________________________")
            for option in options_for_question:
                print(option)

            while True:
                guess1 = input("Enter your first guess: (A,B,C,D)")
                if guess1.upper() in ("A", "B", "C", "D"):
                    break
                else:
                    print("Please enter a valid choice")
                    continue

            if guess1.upper() == answers[question_num][0][0].upper():
                print(
                    f"----------Congratulations!! You gave correct answer for Question No. {question_num}----------")
                score = score + 1
                print("Score:", score)
                amount_won = amount[question_num]
                print(f"----------Your total amount won is: {amount_won}---------")
                print(f"---------------------------------------------------------")
                print(f"----------Let's move to the next question----------------")
                print(f"---------------------------------------------------------")
                continue
            else:
                print("Your first guess is wrong, try one more time")

                while True:
                    use_another_lifeline = (input("Do you wish to use another lifeline:(Y/N)"))
                    if use_another_lifeline.upper() in ("Y", "N"):
                        break
                    else:
                        print("Please enter a valid choice")
                        continue

                if use_another_lifeline.upper() == 'N':
                    for option in options[question_num]:
                        if option.upper().startswith(guess1.upper()):
                            options[question_num].remove(option)
                            print("Remaining options are:")
                    for option in options[question_num]:
                        print(option)
                    guess2 = input("Enter your second guess:")
                    if guess2.upper() == answers[question_num][0][0]:
                        print(
                            f"----------Congratulations!! You gave correct answer for Question No. {question_num}----------")
                        score = score + 1
                        print("Score:", score)
                        amount_won = amount[question_num]
                        print(f"----------Your total amount won is: {amount_won}---------")
                        print(f"---------------------------------------------------------")
                        print(f"----------Let's move to the next question----------------")
                        print(f"---------------------------------------------------------")
                        continue
                    else:
                        print("Your second guess is also wrong")
                        print("You are out of the game")
                        print("Score:", score)
                        print("Amount won:", amount_won)
                        break

                elif use_another_lifeline.upper() == 'Y':
                    if total_lifelines_used < 3:
                        print(
                            "You have chosen Flip the question lifeline as you can not use Double Dip and 50_50 on the same question")
                        lifelines_used['Flip the question'] = True

                        random_index = random.randint(0, len(flip_question) - 1)
                        print("Display the question for flip lifeline:")
                        print(flip_question[random_index])
                        for option in flip_option[random_index]:
                            print(option)
                        total_lifelines_used += 1

                        while True:
                            use_another_lifeline = (input("Do you wish to use another lifeline:(Y/N)"))
                            if use_another_lifeline.upper() in ("Y", "N"):
                                break
                            else:
                                print("Please enter a valid choice")
                                continue

                        if use_another_lifeline.upper() == 'N':

                            while True:
                                guess = input("Please enter your choice: (A,B,C,D)")
                                if guess.upper() in ("A", "B", "C", "D"):
                                    break
                                else:
                                    print("Please enter a valid choice")
                                    continue

                            if guess.upper() == flip_answer[random_index][0][0].upper():
                                print(
                                    f"----------Congratulations!! You gave correct answer for Question No. {question_num}----------")
                                score = score + 1
                                print("Score:", score)
                                amount_won = amount[question_num]
                                print(f"----------Your total amount won is: {amount_won}---------")
                                print(f"---------------------------------------------------------")
                                print(f"----------Let's move to the next question----------------")
                                print(f"---------------------------------------------------------")
                                continue
                            else:
                                print("Incorrect")
                                print("You are out of the game")
                                print("Score:", score)
                                print("Amount won:", amount_won)
                                break

                        elif use_another_lifeline.upper() == 'Y':
                            print("You can only choose 50_50 lifeline")
                            lifelines_used['50_50'] = True
                            total_lifelines_used += 1
                            print(flip_question[random_index])
                            print("_________________________________________________________________")
                            question_options = flip_option[random_index]
                            question_answer = flip_answer[random_index][0]
                            question_options.remove(question_answer)
                            my_list = []
                            my_list.append(question_answer)
                            random_option = random.choice(question_options)
                            my_list.append(random_option)
                            my_list.sort()
                            print("New Options after 50:50 are: ")
                            print(my_list[0])
                            print(my_list[1])
                            guess = input("Enter your answer choice:")
                            if guess.upper() == flip_answer[random_index][0][0].upper():
                                print(
                                    f"----------Congratulations!! You gave correct answer for Question No. {question_num}----------")
                                score = score + 1
                                print("Score:", score)
                                amount_won = amount[question_num]
                                print(f"----------Your total amount won is: {amount_won}---------")
                                print(f"---------------------------------------------------------")
                                print(f"----------Let's move to the next question----------------")
                                print(f"---------------------------------------------------------")
                                continue
                            else:
                                print("Incorrect")
                                print("You are out of the game")
                                break
                    else:
                        print("You have already used all your lifelines")


        elif lifeline_opted == 3 and lifelines_used['Flip the question'] == False:
            lifelines_used['Flip the question'] = True
            print("You have chosen Flip the question lifeline")
            random_index = random.randint(0, len(flip_question) - 1)
            print("Display the question for flip lifeline:")
            print(flip_question[random_index])
            for option in flip_option[random_index]:
                print(option)
            total_lifelines_used += 1

            while True:
                use_another_lifeline = (input("Do you wish to use another lifeline:(Y/N)"))
                if use_another_lifeline.upper() in ("Y", "N"):
                    break
                else:
                    print("Please enter a valid choice")
                    continue

            if use_another_lifeline.upper() == 'N':
                guess = input("Enter your response (A,B,C,D)")
                if guess.upper() == flip_answer[random_index][0][0].upper():
                    print(f"----------Congratulations!! You gave correct answer for Question No. {question_num}----------")
                    score = score + 1
                    print("Score:", score)
                    amount_won = amount[question_num]
                    print(f"----------Your total amount won is: {amount_won}---------")
                    print(f"---------------------------------------------------------")
                    print(f"----------Let's move to the next question----------------")
                    print(f"---------------------------------------------------------")
                    continue
                else:
                    print("Incorrect")
                    print("You are out of the game")
                    print("Score:", score)
                    print("Amount won:", amount_won)
                    break

            elif use_another_lifeline.upper() == 'Y':
                for value in lifeline_choice:
                    if lifelines_used[lifeline_choice[value]] == False:
                        print(value, lifeline_choice[value])
                    else:
                        continue
                chosen_lifeline = int(input("Enter your lifeline choice from the above:"))
                if chosen_lifeline == 1:
                    print("You have chosen 50_50 lifeline")
                    lifelines_used['50_50'] = True
                    total_lifelines_used += 1
                    print(flip_question[random_index])
                    question_options = flip_option[random_index]
                    question_answer = flip_answer[random_index][0]
                    print("_________________________________________________________________")
                    question_options.remove(question_answer)
                    my_list = []
                    my_list.append(question_answer)
                    random_option = random.choice(question_options)
                    my_list.append(random_option)
                    my_list.sort()
                    print("New Options after 50:50 are: ")
                    print(my_list[0])
                    print(my_list[1])
                    guess = input("Enter your answer choice:")
                    if guess.upper() == flip_answer[random_index][0][0].upper():
                        print(
                            f"----------Congratulations!! You gave correct answer for Question No. {question_num}----------")
                        score = score + 1
                        print("Score:", score)
                        amount_won = amount[question_num]
                        print(f"----------Your total amount won is: {amount_won}---------")
                        print(f"---------------------------------------------------------")
                        print(f"----------Let's move to the next question----------------")
                        print(f"---------------------------------------------------------")
                        continue
                    else:
                        print("Incorrect")
                        print("You are out of the game")
                        if score == 5:
                            print("Total Amount won= 10000")
                        elif score < 5:
                            print("Total Amount won= 0")
                        elif score == 10:
                            print("Total Amount won= 32000")
                        elif score < 10 and score > 5:
                            print("Total Amount won= 10000")
                        elif score >= 10:
                            print("Total Amount won:", amount[question_num])

                        print("Score:", score)
                        print("Amount won:", amount_won)
                        print("Total Amount won:", amount[question_num])
                        sys.exit()

                else:
                    print("You have chosen Double dip lifeline")
                    lifelines_used['Double dip'] = True
                    total_lifelines_used += 1
                    for option in flip_option[random_index]:
                        print(option)

                    while True:
                        guess1 = input("Enter your first guess: (A,B,C,D)")
                        if guess1.upper() in ("A", "B", "C", "D"):
                            break
                        else:
                            print("Please enter a valid choice")
                            continue

                    if guess1.upper() == flip_answer[random_index][0][0].upper():
                        print(
                            f"----------Congratulations!! You gave correct answer for Question No. {question_num}----------")
                        score = score + 1
                        print("Score:", score)
                        amount_won = amount[question_num]
                        print(f"----------Your total amount won is: {amount_won}---------")
                        print(f"---------------------------------------------------------")
                        print(f"----------Let's move to the next question----------------")
                        print(f"---------------------------------------------------------")
                        continue
                    else:
                        print("Your first guess is wrong, try one more time")
                        for option in flip_option[random_index]:
                            if option.upper().startswith(guess1.upper()):
                                flip_option[random_index].remove(option)
                                print("Remaining options:")
                                for option in flip_option[random_index]:
                                    print(option)
                                while True:
                                    guess2 = input("Enter your second guess: (A,B,C,D)")
                                    if guess2.upper() in ("A", "B", "C", "D"):
                                        break
                                    else:
                                        print("Please enter a valid choice")
                                        continue

                                if guess2.upper() == flip_answer[random_index][0][0]:
                                    print(
                                        f"----------Congratulations!! You gave correct answer for Question No. {question_num}----------")
                                    score = score + 1
                                    print("Score:", score)
                                    amount_won = amount[question_num]
                                    print(f"----------Your total amount won is: {amount_won}---------")
                                    print(f"---------------------------------------------------------")
                                    print(f"----------Let's move to the next question----------------")
                                    print(f"---------------------------------------------------------")
                                    continue
                                else:
                                    print("Your second guess is also wrong")
                                    print("You are out of the game")
                                    print("Score:", score)
                                    print("Amount won:", amount_won)
                                    break

if score == 5:
    print("Total Amount won= 10000")
elif score < 5:
    print("Total Amount won= 0")
elif score == 10:
    print("Total Amount won= 32000")
elif score < 10 and score > 5:
    print("Total Amount won= 10000")
elif score >= 10:
    print("Total Amount won:", amount[question_num])

else:
    print("Game over!")
def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt<3:
        if guess.lower() == answer.lower():
            #print("Correct answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt<2:
                guess = input("Wrong answer, Please try again.")
            attempt = attempt + 1
    if attempt == 3:
        print("The correct answer is :"+answer)

score = 0
question1 = input("Fastest animal on Earth?")
check_guess(question1,'Cheetah')
question2 = input("Largest animal?")
check_guess(question2,'Blue Whale')
question3 = input("King of animals?")
check_guess(question3,'lion')

print("Your score is: "+str(score))

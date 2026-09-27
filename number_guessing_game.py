import random 

def guessing_game():
    number= random.randint(1,100) #we import random so that we can generate a random  number between 1 to 100
    guesses=[]

    print("\n-----------------------")
    print(" number guessing game")
    print("----------------------")
    print('I have a number chossen between 1 to 100')
    print('you have 7 chances to guess it, good luck')

    while len(guesses)< 7:
        print('\n chances left:', 7-len(guesses))

        try:
            guess= int(input('guess the number:')) #we enter the number that we guessed

            if guess<1 or guess>100:
                print('enter a number between 1 and 100') #if the number is not between 1 and 100
                continue

            if guess in guesses:
                print('you already guessed this number') #if thew number is already guessed
                continue
            guesses.append(guess)

            if guess== number:
                print('\n well done')
                print('you guessed the number correctly') #if the number is guessed correctly
                print('number of guesses:', len(guesses))
                return
            elif guess< number:
                print('your guess is too low') #if the number guessed is less than the number generated
            else:
                print('your guess is too high') #if the number guessed is grater than the generated number 

            print('your guesses:', guesses)

        except ValueError:
            print('wrong input. Enter a number') #if the user enters a string or any other character instead of a number

    print('\n you have used all of your chances. You lost')
    print('the number is:', number)

print('thank you for playing')

while True:
    guessing_game()
    answer= input('play again??(yes/no)')
    if answer.lower()== 'no': #this statement will restart the game if the user selects yes.          
        print('thanks')
        break

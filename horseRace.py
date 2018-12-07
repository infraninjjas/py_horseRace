#!/bin/python
import random
import collections
import sys

horses = {
    "horse 1": random.randint(1, 9999),
    "horse 2": random.randint(1, 9999),
    "horse 3": random.randint(1, 9999),
    "horse 4": random.randint(1, 9999),
    "horse 5": random.randint(1, 9999),
    "horse 6": random.randint(1, 9999),
    "horse 7": random.randint(1, 9999),
    "horse 8": random.randint(1, 9999),
    "horse 9": random.randint(1, 9999),
    "horse 10": random.randint(1, 9999),
    "horse 11": random.randint(1, 9999),
    "horse 12": random.randint(1, 9999),
    "horse 13": random.randint(1, 9999),
    "horse 14": random.randint(1, 9999),
    "horse 15": random.randint(1, 9999),
    "horse 16": random.randint(1, 9999),
    "horse 17": random.randint(1, 9999),
    "horse 18": random.randint(1, 9999),
    "horse 19": random.randint(1, 9999),
    "horse 20": random.randint(1, 9999),
    "horse 21": random.randint(1, 9999),
    "horse 22": random.randint(1, 9999),
    "horse 23": random.randint(1, 9999),
    "horse 24": random.randint(1, 9999),
    "horse 25": random.randint(1, 9999)
}

# Stat Variables
raceCount = 0
guessCount = 0
score = 0

# Player Information
playerName = input('Welcome Player! What is your name?\n>>> ')

# Menu information
print('\n\nGreetings %s, Welcome to the horse race challenge. Here are the rules:\n ' % playerName)
rules = '''
> There are 25 horses
> Each horse has a predetermined finish time, no matter how many times they race
> You may race 5 horses at a time
> After each race, you will receive a printout with the placement of the horses.
>> However, you will not know the time in which they finished

> Your objective is to find the 3 fastest horses, whilst performing as little races as possible.

'''
print(rules)
mainMenu = 'Select an option \n [0] Race\t [1] Guess\t[2] Print Rules\t [9] Exit\n>>> '
subMenu = 'Select 5 horses to race from 1 - 25. (Enter 5 numbers between 1 and 25 separated by spaces)\n>>> '


sort = [(k, horses[k]) for k in sorted(horses, key=horses.get)]
fastestHorses = list()
for k, v in sort:
    fastestHorses.append(k)
userInput = input(mainMenu)
while(userInput != '9'):
    if(userInput == '2'):
        print(rules)
        userInput = input(mainMenu)
    elif(userInput == '0'):
        validInput = "False"
        while(validInput == "False"):
            raceLineup = input(subMenu)
            horsesToRace = raceLineup.split()
            if(len(horsesToRace) == 5):
                validInput = "True"
            else:
                print('You must select 5 horses')
        results = dict()
        i = 0
        while(i < len(horsesToRace)):
            for k, v in sort:
                if(k == ('horse %s' % horsesToRace[i])):
                    results[k] = v
            i += 1
        resultSort = [(k, results[k]) for k in sorted(results, key=results.get)]
        i = 1
        for k, v in resultSort:
            print('%s finished in place %i!' % (k, i))
            i += 1
        raceCount += 1
        print('\nYou have tried %i races so far\n' % raceCount)
        userInput = input(mainMenu)
    elif(userInput == '1'):
        playerGuessed = "False"
        while(playerGuessed == "False"):
            userGuess = input('What are the three fastest horses? (Enter 3 numbers separated with spaces.)\n>>> ')
            guessBreakdown = userGuess.split()
            guessBreakdown = list(map(int, guessBreakdown))
            i = 0
            if(len(guessBreakdown) == 3):
                for g in guessBreakdown:
                    if (('horse %i' % g) == fastestHorses[i]):
                        score += 1
                    i += 1
                playerGuessed = "True"
                guessCount += 1
                print('Your guess count is now: %i' % guessCount)
                if(score == 3):
                    print('Congratulations! You got the 3 fastest horses in %i races and %i guesses' % (raceCount, guessCount))
                    sys.exit()
                else:
                    userInput = input(mainMenu) 
            else:
                print('You must select 3 horses')
    else:
        print('I didn\'t quite get that. Please try again.. ')
        userInput = input(mainMenu)

print("Goodbye")




scores = [[-2 for i in range(5)] for j in range(30)]  # [name, score1, score2, score 3, scoreAverage][personNumber]
userinput = ''  # saves last piece of user input
answer = int()
choice = 'loop'
choice2 = 'error'



def name():  # Function to handle the current user id(if they were already stored in the DB)
    userinput = (str(input('What is your name\n')))
    for i in range(len(scores)+1):

        if i == len(scores):  # Fires when i is one larger than the largest element ID in scores
            for x in range(len(scores)):
                if x == len(scores):
                    print('Not enough lists to store new user, appending list')
                    scores.append([userinput, -2, -2, -2, -2])
                    currentuser = (len(scores) - 1)
                    global currentuser
                    return currentuser


                else:
                    if scores[x][0] == -2:
                        global currentuser
                        currentuser = x
                        scores[x][0] = userinput
                        return currentuser


        if userinput == scores[i][0]:  # user already exists
            global currentuser
            currentuser = i
            return currentuser


            # If the current user is not 0 then its an already existing user


def quiz(counter=0):
    for i in range(1, 2):  #TODO Change to 1,11 so there are 10 questions for real version
        num1 = random.randint(1, 20)  # Generate first random number
        num2 = random.randint(1, 20)  # Generate first random number
        operator = random.choice(["+", "*", "-"])
        print('What is', num1, operator, num2, '?')
        userinput = (input(''))

        if operator is '+':  # if statements to work out what the sumcheck for the answer is
            answer = int(num1 + num2)
        if operator is '-':
            answer = int(num1 - num2)
        if operator is '*':
            answer = int(num1 * num2)
        if int(userinput) == answer:
            print('Correct')
            counter += 1
        else:
            print('Incorrect')
        print('Next question')

    print('You have scored a total of ' + (str(counter)) + '/10')
    return counter


def results_storage():
    counter = quiz()
    print('Now saving you''r results')
    if scores[currentuser][1] == -2:
        scores[currentuser][1] = counter
    else:
        scores[currentuser][3] = scores[currentuser][2]
        scores[currentuser][2] = scores[currentuser][1]
        scores[currentuser][1] = counter


def results_display():
    for i in range(len(scores)):
        if scores[i][0] != -2:
            if scores[i][3] == -2:
                if scores[i][2] == -2:
                    print(str(scores[i][0]), 'Only Recorded Score =', str(scores[i][1]))

                else:
                    print(str(scores[i][0]), 'Newest Score =', str(scores[i][1]), 'Oldest Score=', str(scores[i][2]),
                          'Average score =', str(scores[i][4]))

            else:
                print(str(scores[i][0]), 'Latest score =', str(scores[i][1]), 'Average score =', str(scores[i][4]))


def averages_calculator():
    for i in range(len(scores)):

        if ((scores[i][2]) and (scores[i][3]) == -2) and (scores[i][0]!= -2):
            scores[i][4] = scores[i][1]

        if ((scores[i][3]) == -2) and ((scores[i][2]) > -1)  and (scores[i][0]!= -2):
            scores[i][4] = ((scores[i][2]) + (scores[i][1])) / 2

        if (scores[i][3] >= -1)  and (scores[i][0]!= -2):
            scores[i][4] = ((scores[i][2]) + (scores[i][1]) + (scores[i][3])) / 3
def readwrite():
    saveFile = open('results.txt', 'w')
    for i in range(len(scores)):
        if scores[i][1] != -2:
            for x in range(5):
                saveFile.write(str(scores[i][x]))
                saveFile.write(' ')
            saveFile.write('\n')

    saveFile.close


# Start of Program
while choice == 'loop':
    import random

    name()  # Runs Name function
    print('Lets start the maths quiz!')
    results_storage()
    choice2 = 'error'
    while choice2 == 'error':
        choice2 = input(
            'Would you like to display all the results, repeat for a new user or save data to a file? \nType ''repeat'' or ''display'' or ''save''\n')
        if choice2 == 'repeat':
            choice = 'loop'
            break
        if choice2 == 'display':
            averages_calculator()
            results_display()
            break
        if choice2 == 'save':
            readwrite()
            break
        if choice2 != 'loop' or 'display':
            print('Sorry that was an invalid choice, please try again')


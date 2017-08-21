#written by usingpython.com

#allows us to access a random 'key' in the dictionary
import random

number_1_ans = 0
number_2_ans = 0
number_3_ans = 0
number_4_ans = 0

#the questions/answer dictionary
my_dict =   {
                "What is your favorite animal 1) serpent 2) badger 3) lion 4) eagle" : "I don't know",
                "How would you describe yourself 4) creativity and wit 2) loyal and dedicated 3) bravery and courage 1) cunning and a leader" : "I don't know",
                "What is your favorite color 3) scarlet and gold 2) yellow and black 1) green and silver 4) blue and bronze" : "I don't know",
                "What is your favorite element 2) earth 3) fire 1) water 4) air" : "I don't know",
                "What is would be your favorite hogwarts subject 4) charms 1) potions or defence against the dark arts 3) transfiguration or defence against the dark arts 2) herbology" : "I don't know",
             }

#welcome message
print("Computing Revision Quiz")
print("=======================")

#the quiz will end when this variable becomes 'False'
playing = True

#While the game is running
while playing == True:

    #set the score to 0
    score = 0

    #gets the number of questions the player wants to answer
    num = int(input("\nHow many questions would you like: "))

    #loop the correct number of times
    for i in range(num):

        #the question is one of the dictionary keys, picked at random
        question = (random.choice( list(my_dict.keys())))
        #the answer is the string mapped to the question key
        answer = my_dict[question]

        #print the question, along with the question number
        print("\nQuestion " + str(i+1) )
        print(question  + "?")

        #get the user's answer attempt
        guess = input("> ")

        if guess == "1": 
            number_1_ans = number_1_ans +1
        elif guess == "2":
            number_2_ans = number_2_ans +1
        elif guess == "3":
            number_3_ans = number_3_ans +1
        else:
            number_4_ans = number_4_ans +1
            
            

        #if their guess is the same as the answer
        if guess.lower() == answer.lower():
            #add 1 to the score and print a message
            print("Okay!")
            score += 1
        else:
            print("Okay!")

    #after the quiz, print their final score  
    print("\nYour final I don't know score is:" + str(score))
    print("Your Slitherin score is: %s" % number_1_ans)
    print("Your Hufflepuff score is: %s" % number_2_ans)
    print("Your Gryffindor scoce is: %s" % number_3_ans)
    print("Your Ravenclaw score is: %s" % number_4_ans)
    

    #store the user's input...
    again = input("Enter any key to play again, or 'q' to quit.")


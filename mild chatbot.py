
import random
print("Welcome to Mo's Chatbot. What's on your mind today?")
doExit = False

while doExit == False:
    choice = input()
    if choice == "quit":
        doExit = True
        break

    #listen and respond to feelings
    if choice.find("sad") != -1 or choice.find("feeling down") != -1 or choice.find("upset") != -1 or choice.find("angry") != -1 :
        print("I'm sorry to hear you're feeling that way.")
    elif choice.find("happy") != -1 or choice.find("glad") != -1 or choice.find("excited") != -1 or choice.find("looking forward") != -1 :
        print("That's great!")
    elif choice.find("I'm") != -1: #these next three lines let you repeat the word after "I'm" back in a sentence
        word_list = choice.split() #break the sentence into a list with one word per slot
        next_word = word_list[word_list.index("I'm")+1] #find the word after "I'm"
        print("Why are you", next_word+ "?") #repeat it back 
        #NOTE: it would be good to add an if statement here checking if the next word was "a" 
        #so if someone says "I'm a frog", it doesn't say back, "Why are you a?"
    if choice.find("burgers") != -1 or choice.find("pizza") != -1 or choice.find("ramen") != -1 or choice.find("crepes"):
        print("i like that food too.")
    #listen and respond to specific topics
    elif   choice.find("dad") != -1 or choice.find("brother") != -1 or choice.find("sister") != -1 :
        print("Tell me more about your family.")
    elif choice.find("java") != -1:
        print("i see you are part of the javascript fandom")
    elif choice.find ("mom"):
        num = random.randrange(1,2)
        if num == 1:
            print ("hey siri tell me a yo mama joke")

        else:
            print("yo momma so fat she made a bean and cheese burrito scared")
    elif choice.find("dog") != -1 or choice.find("cat") != -1 or choice.find("fish") != -1 or choice.find("bird") != -1 :
        print("I'd like to hear more about this pet.")

    else: #randomize last statement so it's not too repetetive 
        num = random.randrange(1, 100)
        if num <50:
            print("Can you tell me more?")
        else:
            print("What does that suggest to you?")

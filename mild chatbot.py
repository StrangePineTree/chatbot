
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

    #listen and respond to specific topics
    if choice.find("mom") != -1 or choice.find("dad") != -1 or choice.find("brother") != -1 or choice.find("sister") != -1 :
        print("Tell me more about your family.")

    elif choice.find("dog") != -1 or choice.find("cat") != -1 or choice.find("fish") != -1 or choice.find("bird") != -1 :
        print("I'd like to hear more about this pet.")

    else: #randomize last statement so it's not too repetetive 
        num = random.randrange(1, 100)
        if num <50:
            print("Can you tell me more?")
        else:
            print("What does that suggest to you?")

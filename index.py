# import os

# if __name__=='__main__':
 
#  while(True):

#     x=input("What you want me to Speak: ")
#     print("Welcome to Robo Speaker 1.2. Created by SAMAR ABBAS")
#     command=f"say {x}"
#     os.system(command)

import pyttsx3

if __name__ == '__main__':

    while(True):
        x = input("What do you want me to speak: ")
        print("Welcome to Robo Speaker 1.2. Created by SAMAR ABBAS")
        if(x=='clear'):
            # engine.say("Bye My Friend")
            break

        # Initialize the text-to-speech engine
        engine = pyttsx3.init()

        # Set properties (optional)
        # engine.setProperty('rate', 150)  # Speed of speech

        # Speak the user input
        engine.say(x)

        # Wait for the speech to finish
        engine.runAndWait()

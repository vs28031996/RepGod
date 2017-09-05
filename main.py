from spy_details import spy
from start_chat import start_chat

question = "Continue as %s %s (Y/N)" % (spy['salutation'], spy['name'])
existing = raw_input(question)

# validating user's input
if existing == "Y" or existing == "y":
    start_chat(spy['name'], spy['age'], spy['rating'])

elif existing == "N" or existing == "n":
    spy['name'] = raw_input("Provide your name here :")

    if len(spy['name']) > 0:
        spy['salutation'] = raw_input("What should we call you? : ")
        spy['name'] = spy['salutation'] + " " + spy['name']
        spy['age'] = 0
        spy['rating'] = 0.0
        spy['is_online'] = False
        spy['age'] = raw_input("What is your age? ")
        spy['age'] = int(spy['age'])
        if type(spy['age']) is int:
            if 12 < spy['age'] < 50:
                spy['rating'] = raw_input(" What is your spy rating: ")
                spy['rating'] = float(spy['rating'])
                if spy['rating'] > 4.5:
                    print " Great ace!!"
                elif 3.5 < spy['rating'] < 4.5:
                    print " You are Good one "
                elif 2.5 < spy['rating'] < 3.5:
                    print " You can always do better"
                else:
                    print " We can always use somebody to help in the office"
                print " Welcome " + spy['name'] + " Glad to have u back"
                print "Let's get Started!"
                start_chat(spy['name'], spy['age'], spy['rating'])
            else:
                print " You are not eligible to a spy"
        else:
            print " Please type a valid number "

    else:
        print "Invalid Name Try again"
else:
    print " Wrong choice.Try again"



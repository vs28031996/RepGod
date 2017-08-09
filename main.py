print "Let's get Started!"
spy_name = raw_input("Provide your name here :")

if len(spy_name) > 0:
    spy_salutation = raw_input("What should we call you? : ")
    spy_name = spy_salutation + " " + spy_name
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False
    spy_age = raw_input("What is your age? ")
    spy_age = int(spy_age)
    if 12 < spy_age < 50:


    print "Alright " + spy_name + " i'd like to know more about you"
    print "Welcome " + spy_name + " Glad to have u back"

else:
    print "Invalid Name Try again"










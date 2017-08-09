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
    if type(spy_age) is int:
        if 12 < spy_age < 50:
            spy_rating = raw_input(" What is your spy rating: ")
            spy_rating = float(spy_rating)
            if spy_rating >4.5 :
                print " Great ace!!"
            elif 3.5 < spy_rating < 4.5:
                print " You are Good one "
            elif 2.5 < spy_rating < 3.5:
                print " You can always do better"
            else:
                print " We can always use somebody to help in the office"
            print " Alright " + spy_name + " i'd like to know more about you"
            print " Welcome " + spy_name + " Glad to have u back"

        else:
            print " You are not eligible to a spy"
    else:
        print " Please type a valid number "

else:
    print "Invalid Name Try again"

spy_is_online = True

print " Authentication Complete . Welcome : %s Age : %d and rating of : %f " % (spy_name, spy_age, spy_rating)













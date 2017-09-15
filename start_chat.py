# Start_Chat Function definition
from add_status import add_status, status
from add_friends import add_friend
from spy_details import  spy


def start_chat(name, age, rating):
    current_status = " "

    print "Let's get Started!"
    print " Authentication Complete . Welcome : %s Age : %d and " \
          "rating of : %.2f " % (spy['name'], spy['age'], spy['rating'])

    show_menu = True
    while show_menu:
        menu_choices = " What do you want to do? : \n 1.Add Status  \n 2. Add a friend \n 3. Send a secret message " \
                       "4. Read a secret message \n 5. Read Chats from user \n 2.Close Application \n "
        result = int(raw_input(menu_choices))
        # validating user input
        if result == 1:
            # action 1
            if len(current_status) > 1:
                current_status = add_status(current_status, status)
            else:
                status_message = None
                current_status = add_status(status_message, status)
                print " %s " % current_status

        elif result == 2:
            show_menu = False
        else:
            print " Wrong choice .Try again"



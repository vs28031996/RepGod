# Start_Chat Function definition
from add_status import add_status, status
from add_friends import add_friend
from send_message import send_message
from read_message import read_message
from read_chat import read_chat
from globals import spy


def start_chat(name, age, rating):
    current_status = " "

    print "Let's get Started!"
    spy.name = spy.salutation + ' ' + spy.name
    print " Authentication Complete . Welcome : %s Age : %d and " \
          "rating of : %.2f " % (spy.name, spy.age, spy.rating)

    show_menu = True
    while show_menu:
        menu_choices = " What do you want to do? : \n 1. Add Status  \n 2. Add a friend \n 3. Send a secret message " \
                       "\n 4. Read a secret message \n 5. Read Chats from user \n 6. Close Application \n "
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
            friends_added = add_friend()
            print "You have %d Friend "%(friends_added)

        elif result == 3:
            send_message()

        elif result == 4:
            read_message()

        elif result == 5:
            read_chat()

        elif result == 6:
            print "Goodbye my friend."
            break

        else:
            print " Wrong choice .Try again"



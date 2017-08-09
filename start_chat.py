# Start_Chat Function definition
from add_status import add_status


def start_chat(name, age, rating):
    show_menu = True
    while show_menu:
        menu_choices = " What do you want to do? : \n 1.Add Status  \n 2.Close Application \n "
        result = int(raw_input(menu_choices))
        # validating user input
        if result == 1:
            # action 1
            status_message = None
            current_status = add_status(status_message)
            print " %s " % current_status
            show_menu = False
        elif result == 2:
            show_menu = False
        else:
            print " Wrong choice .Try again"



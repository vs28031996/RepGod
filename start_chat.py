# Start_Chat Function definition
def start_chat(name, age, rating):
    show_menu = True
    while show_menu:
        menu_choices = " What do you want to do? : \n 1.Add Status  \n 2.Close Application \n "
        result = int(raw_input(menu_choices))
        # validating user input
        if result == 1:
            # action 1
            pass
        elif result == 2:
            show_menu = False
        else:
            print " Wrong choice .Try again"



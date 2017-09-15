from globals import status


def add_status(status_message, status1):
    if status_message is None:
        print " You don't have any status \n"
    else:
        print " Your current status is %s \n " % status_message
    default = raw_input(" Do you want to select from older status(Y/N) :")

    if default == "n" or default == "N":
        new_status_message = raw_input(" What status message do you want to set?: ")

        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            status.append(updated_status_message)

    elif default == "y" or default == "Y":
        item_position = 1
        for message in status1:
            print " %d. %s " % (item_position, message)
            item_position += 1
        message_selection = int(raw_input(" \nChoose from the above messages : "))
        if len(status) >= message_selection:
            updated_status_message = status1[message_selection - 1]

    return updated_status_message







from globals import friends


def select_a_friend():
    # For index of elements
    item_number = 0
    # Printing all friends
    for friend in friends:
        print " %d. %s aged %d with rating %.2f is online " % \
              (item_number+1, friend.name, friend.age, friend.rating)
        item_number = item_number + 1
    while True:
        # Exception handling
        try:
            friend_choice = int(raw_input("Choose from your friends: "))
            break
        except StandardError:
            print "Enter valid entry"
    friend_choice_position = friend_choice - 1
    return friend_choice_position







from globals import friends


def select_a_friend():
    item_number = 0
    for friend in friends:
        print " %d. %s aged %d with rating %.2f is online " % (item_number+1, friend['name'], friend['age'], friend['rating'])
        item_number = item_number + 1
        friend_choice = int(raw_input("Choose from your friends: "))
        friend_choice_position = friend_choice - 1
        return friend_choice_position







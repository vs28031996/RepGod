from select_friend import select_a_friend
from globals import friends
from termcolor import colored


def read_chat():
    read_for = select_a_friend()
    # Reading chat history of a friend
    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print(colored(str('[%s] %s %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)), 'blue'))
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)
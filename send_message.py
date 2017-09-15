
from select_friend import select_a_friend
from steganography.steganography import Steganography
from globals import friends, ChatMessage
import re


def send_message():

    # Use of Steganography
    friend_choice = select_a_friend()
    original_image = raw_input("What is the name of the image to hide the message? : ")
    pattern = '^[a-zA-Z]+\.jpg$'
    if re.match(pattern, original_image) != None:
        output_image = raw_input("Provide output image file name?")
        while True:
            text = raw_input("Enter your message here?")
            if len(text) > 0:
                Steganography.encode(original_image, output_image, text)
                break

    else:
        print "Invalid image name. try .jpg images only."

    new_chats = ChatMessage(text, True)

    friends[friend_choice].chats.append(new_chats)
    print "Your secret message is ready"
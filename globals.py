from spy_details import Spy
from datetime import datetime


status = ['My name is Bond, James Bond', ' I C Python', 'Its gonna blow']

# Spy object
spy = Spy("Das", "Mr. ", 31, 2.1)

# Friends
friend_one = Spy('Robin', 'Mr.', 21, 4)
friend_two = Spy('Malini', 'Ms.', 21, 5)
friend_three = Spy('Ganpat Rai', 'Dr.', 50, 4.5)

friends = [friend_one, friend_two, friend_three]

# Class to store Chat messages


class ChatMessage:

  def __init__(self, message, sent_by_me):
    self.message = message
    self.time = datetime.now()
    self.sent_by_me = sent_by_me


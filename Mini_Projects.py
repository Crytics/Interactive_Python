############################################
# Python Trainer
# ---------------------------------
# Created by  : Adam Nguyen
# Updated by  : Adam Nguyen
# Created at  : 10/31/2014
# Updated at  : xx/xx/xxxx
# Description : Python Examples
#############################################


###Mouseclicks
import simplegui, math

width = 450
height = 300
ball_pos = [width / 2, height / 2]
ball_radius = 15
ball_color = "blue"

def distance(p, q):
    return math.sqrt( (p[0] - q[0])**2 + (p[1] - q[1])**2)


def click(pos):
    global ball_pos, ball_color
    if distance(pos, ball_pos) < ball_radius:
        ball_color = "Green"
    else:
        ball_color = "blue"
        ball_pos = list(pos) #creates a new copy and modify at a later date


def draw(canvas):
    canvas.draw_circle(ball_pos, ball_radius, 1, "black", ball_color)

frame = simplegui.create_frame("Mouse selection", width, height)
frame.set_canvas_background("white")
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

frame.start()


###List Methods
import simplegui

tasks = []

def clear():
    global tasks
    tasks = []

def new(task):
    tasks.append(task)

def remove_num(tasknum):
    try:
        n = int(tasknum)
        if n > 0 and n <= len(tasks):
            tasks.pop(n-1)
    except:
        pass

def remove_name(taskname):
    try:
        tasks.pop(tasks.index(taskname))
    except:
        pass

#    if taskname in tasks:
#        tasks.remove(taskname)

def draw(canvas):
    print tasks

frame = simplegui.create_frame("Task List", 600, 400)

frame.add_input("New task:", new, 200)
frame.add_input("Remove task number:", remove_num, 200)
frame.add_input("Remove task:", remove_name, 200)
frame.add_button("Clear All", clear)
frame.set_draw_handler(draw)

frame.start()



###Click to add balls
import simplegui, math

width = 450
height = 300
ball_list = []
ball_radius = 15
ball_color = "blue"

def distance(p, q):
    return math.sqrt( (p[0] - q[0])**2 + (p[1] - q[1])**2)


def click(pos):
    changed = False
    for ball in ball_list:
        if distance([ball[0], ball[1]], pos) < ball_radius:
            ball[2] = "green"
            changed = True
    if not changed:
        ball_list.append([pos[0], pos[1], "blue"])


def draw(canvas):
    for ball in ball_list:
        canvas.draw_circle([ball[0], ball[1]], ball_radius, 1, "black", ball[2])

frame = simplegui.create_frame("Mouse selection", width, height)
frame.set_canvas_background("white")
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

frame.start()



###Reclick to remove
import simplegui, math

width = 450
height = 300
ball_list = []
ball_radius = 15
ball_color = "blue"

def distance(p, q):
    return math.sqrt( (p[0] - q[0])**2 + (p[1] - q[1])**2)


def click(pos):
    remove = [] #Create list of variables you want to remove
    for ball in ball_list:
        if distance(ball, pos) < ball_radius:
            remove.append(ball)
    if remove == []:
        ball_list.append(pos)
    else:
        for ball in remove:
            ball_list.pop(ball_list.index(ball))


def draw(canvas):
    for ball in ball_list:
        canvas.draw_circle(ball, ball_radius, 1, "black", ball_color)

frame = simplegui.create_frame("Mouse selection", width, height)
frame.set_canvas_background("white")
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

frame.start()



###Iterating over lists
number = [1, 7, 2, 34, 8, 7, 2, 5, 14, 22, 93, 48, 76, 15, 7]

def count_odd(numbers):
    count = 0
    for i in numbers:
        if  i % 2 > 0:
            count += 1
    print count

def count_even(numbers):
    count = 0
    for i in numbers:
        if  i % 2 == 0:
            count += 1
    print count

def check_odd(numbers):
    for i in numbers:
        if i % 2 == 1:
            print True
            break
    print False

def remove_odd(numbers):
    remove = []
    for i in numbers:
        if  i % 2 > 0:
            remove.append(i)
    for j in remove:
            numbers.pop(numbers.index(j))
    print numbers


count_odd(number)
check_odd(number)
count_even(number)
remove_odd(number)


###Loading images
import simplegui

URL = 'http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg'
image = simplegui.load_image(URL)

map_width = 1521
map_height = 1818
scale = 3
can_width = map_width // scale
can_height = map_height // scale
mag_size = 120
mag_pos = [can_width // 2, can_height // 2]

def click(pos):
    global mag_pos
    mag_pos = list(pos)


def draw(canvas):
    canvas.draw_image(image,
                [map_width // 2, map_height // 2], [map_width, map_height],
                [can_width // 2, can_height // 2], [can_width, can_height])

    map_center = [scale * mag_pos[0], scale * mag_pos[1]]
    map_rectangle = [mag_size, mag_size]
    mag_center = mag_pos
    mag_rectangle = [mag_size, mag_size]
    canvas.draw_image(image, map_center, map_rectangle, mag_center, mag_rectangle)


frame = simplegui.create_frame("Map magnifier", can_width, can_height)

frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)
frame.start()



###Blackjack
# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.Hand = []	# create Hand object

    def __str__(self):
        return "Hand contains " + str(self.Hand)	# return a string representation of a hand

    def add_card(self, card):
        self.Hand.append(card)	# add a card object to a hand

    def get_value(self):
        values = 0
        rank = []
        for card in self.Hand:
            values += VALUES[card.rank]
            rank.append(card.rank)
        while values <= 21:
            if ("A" not in rank) or (values + 10 > 21):
                return values
            else:
                return values + 10
        
    def draw(self, canvas, pos):
        for card in self.Hand:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0]/4 + CARD_CENTER[0], pos[1]/4 + CARD_CENTER[1]], CARD_SIZE)
        
# define deck class 
class Deck:
    def __init__(self):
        pass	# create a Deck object

    def shuffle(self):
        # shuffle the deck 
        pass    # use random.shuffle()

    def deal_card(self):
        pass	# deal a card object from the deck
    
    def __str__(self):
        pass	# return a string representing the deck



#define event handlers for buttons
def deal():
    global outcome, in_play

    # your code goes here
    
    in_play = True

def hit():
    pass	# replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    pass	# replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    card = Card("S", "A")
    card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric

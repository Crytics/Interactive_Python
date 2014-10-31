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




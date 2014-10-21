############################################
# Pong
# ---------------------------------
# Created by  : Adam Nguyen
# Updated by  : Adam Nguyen
# Created at  : 10/20/2014
# Updated at  : xx/xx/xxxx
# Description : Interactive Python
#############################################

#Implement with: http://www.codeskulptor.org/

# Implementation of classic arcade game Pong
import simplegui

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 1100 #600
HEIGHT = 700 #400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 150
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [3, 3]
paddle1_vel = 75
score1 = 0
score2 = 0
paddle1_pos = [[0, (HEIGHT - PAD_HEIGHT) / 2], [0, HEIGHT - (HEIGHT - PAD_HEIGHT) / 2]]
paddle2_pos = [[WIDTH, (HEIGHT - PAD_HEIGHT) / 2], [WIDTH, HEIGHT - (HEIGHT - PAD_HEIGHT) / 2]]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos, ball_vel # these are vectors stored as lists
    #Spawn settings
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    paddle1_pos = [[0, (HEIGHT - PAD_HEIGHT) / 2], [0, HEIGHT - (HEIGHT - PAD_HEIGHT) / 2]]
    paddle2_pos = [[WIDTH, (HEIGHT - PAD_HEIGHT) / 2], [WIDTH, HEIGHT - (HEIGHT - PAD_HEIGHT) / 2]]

# define event handlers
def key_handler(key):
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    # update paddle's vertical position, keep paddle on the screen
    if key == simplegui.KEY_MAP['q']:
        paddle1_pos[0][1] -= paddle1_vel
        paddle1_pos[1][1] -= paddle1_vel
    elif key == simplegui.KEY_MAP['a']:
        paddle1_pos[0][1] += paddle1_vel
        paddle1_pos[1][1] += paddle1_vel
    elif key == simplegui.KEY_MAP['p']:
        paddle2_pos[0][1] -= paddle1_vel
        paddle2_pos[1][1] -= paddle1_vel
    elif key == simplegui.KEY_MAP['l']:
        paddle2_pos[0][1] += paddle1_vel
        paddle2_pos[1][1] += paddle1_vel

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    elif (ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS)) and ((ball_pos[1] >= paddle1_pos[0][1]) and (ball_pos[1] <= paddle1_pos[1][1])):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] += 1
    elif (ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS)) and ((ball_pos[1] >= paddle2_pos[0][1]) and (ball_pos[1] <= paddle2_pos[1][1])):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] -= 1
    elif (ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS)) and ((ball_pos[1] <= paddle1_pos[0][1]) or (ball_pos[1] >= paddle1_pos[1][1])):
        score1 += 1
        ball_vel = [3, 3]
        spawn_ball()
    elif (ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS)) and ((ball_pos[1] <= paddle2_pos[0][1]) or (ball_pos[1] >= paddle2_pos[1][1])):
        score2 += 1
        ball_vel = [3, 3]
        spawn_ball()
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 10, 'white')
    # draw paddles
    canvas.draw_polyline(paddle1_pos, 12, 'white')
    canvas.draw_polyline(paddle2_pos, 12, 'white')
    # draw scores
    canvas.draw_text(str(score1), (WIDTH / 3, 100), 30, 'white')
    canvas.draw_text(str(score2), (WIDTH * 2/3, 100), 30, 'white')

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keyup_handler(key_handler)

# start frame
frame.start()

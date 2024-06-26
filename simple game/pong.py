# Implementation of classic arcade game Pong

import simpleguitk as simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
flag = True
paddle1_vel = paddle2_vel = 0
paddle1_pos = paddle2_pos = (HEIGHT - PAD_HEIGHT) / 2
score1 = score2 = 0
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel[0] = random.randrange(120, 240)/100
    ball_vel[1] = -random.randrange(60, 180)/100
    if direction == 'left':
        ball_vel[0] = -ball_vel[0]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  
    paddle1_pos = paddle2_pos = paddle1_vel = paddle2_vel = score1 = score2 = 0
    spawn_ball('left')

    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1]<= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Red", "Red")
    
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos <= HEIGHT - PAD_HEIGHT - paddle1_vel and paddle1_vel >0) or (paddle1_pos>0 and paddle1_vel <0):
        paddle1_pos += paddle1_vel
    if (paddle2_pos <= HEIGHT - PAD_HEIGHT - paddle2_vel and paddle2_vel >0) or (paddle2_pos>0 and paddle2_vel <0):
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos],[0, PAD_HEIGHT+paddle1_pos],[PAD_WIDTH, PAD_HEIGHT+paddle1_pos],[PAD_WIDTH, paddle1_pos]], 1, 'Blue', 'Blue')
    canvas.draw_polygon([[WIDTH - PAD_WIDTH,paddle2_pos],[WIDTH - PAD_WIDTH,PAD_HEIGHT+paddle2_pos],[WIDTH, PAD_HEIGHT+paddle2_pos],[WIDTH, paddle2_pos]], 1, 'Blue', 'Blue')
    
    # determine whether paddle and ball collide    
    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        if paddle2_pos < ball_pos[1] < PAD_HEIGHT + paddle2_pos:
            ball_vel[0] = -ball_vel[0]*1.1
        else:
            score1 += 1
            spawn_ball('right')
            
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if paddle1_pos < ball_pos[1] < PAD_HEIGHT + paddle1_pos:
            ball_vel[0] = -ball_vel[0]*1.1
        else:
            score2 += 1
            spawn_ball('left')
    
    # draw scores
    canvas.draw_text(str(score1),[WIDTH / 2 - 150, 80],40,'Green')
    canvas.draw_text(str(score2),[WIDTH / 2 + 150, 80],40,'Green')
        
    
def keydown(key):
    global paddle1_vel, paddle2_vel, flag
    # if flag and key == simplegui.KEY_MAP['space']:
        # flag = False
        # new_game()
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel -= 5
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel += 5
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel -= 4
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel += 4

        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w'] or key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart',new_game,200)
# frame.add_label('Press space to START!!!')

new_game()
frame.start()
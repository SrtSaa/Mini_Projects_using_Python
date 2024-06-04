import simpleguitk as simplegui
import random

# helper function to initialize globals
def new_game():
    global cards, f_cards, state, turns
    cards = [i for i in range(8)]*2
    random.shuffle(cards)   
    f_cards = list('f'*16)  
    state = turns = 0

     
# define event handlers
def mouseclick(pos):
    global cards, f_cards, state, turns, prev1, prev2
    if state == 0:
        f_cards[pos[0]//50] = 't'  
        prev1 = pos[0]//50     
        state = 1
    elif state == 1:
        if f_cards[pos[0]//50] == 'f':
            turns += 1
            f_cards[pos[0]//50] = 't'
            prev2 = pos[0]//50     
            state = 2
    else:       
        if f_cards[pos[0]//50] == 'f':
            if cards[prev1] != cards[prev2]:       
                f_cards[prev1] = f_cards[prev2] = 'f'
            f_cards[pos[0]//50] = 't'  
            prev1 = pos[0]//50
            state = 1
    
                          
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards, f_cards, turns
    # first displays the number
    for card_index in range(len(cards)):
        card_pos = 50*card_index + 15       
        canvas.draw_text(str(cards[card_index]),(card_pos,60),30,'white')
        for i in range(16):
            if f_cards[i] == 'f':
                canvas.draw_polygon([[i*50,0],[i*50+50,0],[i*50+50,100],[i*50,100]],5,'red','green')
        label.set_text('Turns = '+str(turns))


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


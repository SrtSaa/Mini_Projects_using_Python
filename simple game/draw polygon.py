import simpleguitk as sg

polyline = []


def draw(canvas):
    global polyline
    if len(polyline)>0:
        canvas.draw_circle(polyline[0],1,1,'white','white')
        canvas.draw_polyline(polyline,2,'white')

def clear():
    global polyline 
    polyline = []

def click(pos):
    global polyline
    polyline.append(pos)

frame = sg.create_frame("home",300,300)
frame.set_draw_handler(draw)
frame.add_button('Clear',clear)
frame.set_mouseclick_handler(click)

frame.start()

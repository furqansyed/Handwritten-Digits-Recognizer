# from pynput.mouse import Listener

# def on_move(x, y):
#     print('Pointer moved to {0}'.format(
#         (x, y)))

# def on_click(x, y, button, pressed):
#     print('{0} at {1}'.format(
#         'Pressed' if pressed else 'Released',
#         (x, y)))
#     if not pressed:
#         # Stop listener
#         return False

# def on_scroll(x, y, dx, dy):
#     print('Scrolled {0}'.format(
#         (x, y)))

# # Collect events until released
# with Listener(
#         # on_move=on_move,
#         on_click=on_click,
#         on_scroll=on_scroll) as listener:
#     listener.join()



# from tkinter import *

# def motion(event):
#   print("Mouse position: (%s %s)" % (event.x, event.y))
#   return

# master = Tk()
# whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
# msg = Message(master, text = whatever_you_do)
# msg.config(bg='lightgreen', font=('times', 24, 'italic'))
# msg.bind('<Motion>',motion)
# msg.pack()
# mainloop()



#!/usr/bin/python3
# write tkinter as Tkinter to be Python 2.x compatible
from tkinter import *
def hello(event):
    print("Single Click, Button-l")
    # print(motion(event))

def motion(event):
    return(event.x, event.y)

def drag(event):
    print(event.x)

def quit(event):                           
    print("Double Click, so let's stop") 
    import sys; sys.exit() 

widget = Button(None, text='Mouse Clicks')
widget.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quit) 
widget.bind('<B1-Motion>', drag)
widget.mainloop()
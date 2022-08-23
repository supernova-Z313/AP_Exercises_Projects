from tkinter import *


root = Tk()
root.title("AP4002 Pong Game")

canvas = Canvas(root, width=500, height=320, bg='turquoise')
canvas.grid(row=0, column=0)

ball = canvas.create_oval(30, 30, 50, 50, fill="yellow")

bat = canvas.create_rectangle(0, 310, 100, 320, fill="blue")
ball_pos = canvas.coords(ball)


def move_bat(event):
    if event.keysym == 'Right':
        canvas.move(bat, 10, 0)
    elif event.keysym == 'Left':
        canvas.move(bat, -10, 0)


def move_ball(event):
    if event.keysym == "Up":
        canvas.move(ball, 0, -5)
    elif event.keysym == "Down":
        canvas.move(ball, 0, 20)


canvas.bind("<Down>", move_ball)
# canvas.bind_all("<Up>", move_ball)
#
# canvas.bind_all('<Right>', move_bat)
# canvas.bind_all('<Left>', move_bat)

root.mainloop()

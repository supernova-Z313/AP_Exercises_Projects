import tkinter as tk
from tkinter import Menu, IntVar, ttk, scrolledtext, messagebox
import os
from random import choice


class GameObject(object):
    all_item = []

    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    def get_position(self):
        return self.canvas.coords(self.item)

    def move(self, x, y):
        self.canvas.move(self.item, x, y)

    def delete(self):
        self.canvas.delete(self.item)


class Ball(GameObject):
    def __init__(self, canvas, x, y, speed: int = 50):
        self.canvas = canvas
        self.radius = 3
        self.speed = speed
        self.ball = self.canvas.create_oval(x - self.radius, y - self.radius, x + self.radius, y + self.radius
                                            , fill="yellow")
        self.item = self.ball
        self.x = 0
        self.y = 0
        self.start = True
        self.list_of_f = []
        GameObject.all_item.append(self)

    def update(self, bat, cls):
        if not(cls.state_game):
            pass
        else:
            p = self.get_position()
            b_p = bat.get_position()

            if self.start:
                self.x, self.y = choice([2, -2]), choice([2, -2])
                self.start = False
            elif int(p[3]) >= 314:
                self.start = True
                cls.win_loss(False, False)
            elif int(p[0]) <= 10:
                self.x = -self.x
            elif int(p[1]) <= 10:
                self.y = -self.y
            elif int(p[2]) >= 492:
                self.x = -self.x

            # for top of rocket
            elif int(b_p[0]) <= int(p[2]) and int(b_p[2]) >= int(p[0]) and int(p[3]) == int(b_p[1]):
                self.y = -self.y

            # for side of rocket
            elif b_p[1] <= int(p[1]) <= b_p[3] and (int(p[2]) == int(b_p[0]+1) or int(p[2]) == int(b_p[0]-1) or
                                                    int(p[0]) == int(b_p[2]+1) or int(p[0]) == int(b_p[2]-1)):
                self.x = -self.x
            elif b_p[1] <= int(p[3]) <= b_p[3] and (int(p[2]) == int(b_p[0]+1) or int(p[2]) == int(b_p[0]-1) or
                                                    int(p[0]) == int(b_p[2]+1) or int(p[0]) == int(b_p[2]-1)):
                self.x = -self.x

            else:
                for i in GameObject.all_item:
                    if not(isinstance(i, Ball) or isinstance(i, Bat)):
                        i_p = i.get_position()
                        p_x = (p[0] + p[2])/2
                        p_y = (p[1] + p[3])/2
                        if i_p[0] <= p_x+1 <= i_p[2] and (int(p[1]+1) == int(i_p[3]) or int(p[1]) == int(i_p[3]) or
                                                          int(p[3]+1) == int(i_p[1]) or int(p[3]) == int(i_p[1])):
                            self.y = -self.y
                            i.hit()
                            if i.hits <= 0:
                                GameObject.all_item.remove(i)
                        elif i_p[1] <= p_y+1 <= i_p[3] and (int(p[0]+1) == int(i_p[2]) or int(p[0]) == int(i_p[2]) or
                                                            int(p[2]+1) == int(i_p[0]) or int(p[2]) == int(i_p[0])):
                            self.x = -self.x
                            i.hit()
                            if i.hits <= 0:
                                GameObject.all_item.remove(i)

                        elif i_p[0] <= p[0]+1 <= i_p[2] and (int(p[1]+1) == int(i_p[3]) or int(p[1]) == int(i_p[3])):
                            self.x = -self.x
                            self.y = -self.y
                            i.hit()
                            if i.hits <= 0:
                                GameObject.all_item.remove(i)
                        elif i_p[0] <= p[0]+self.radius-1 <= i_p[2] and (int(p[1]+1) == int(i_p[3]) or int(p[1]) == int(i_p[3])):
                            self.x = -self.x
                            self.y = -self.y
                            i.hit()
                            if i.hits <= 0:
                                GameObject.all_item.remove(i)
                        elif i_p[0] <= p[2]-1 <= i_p[2] and (int(p[3]-1) == int(i_p[1]) or int(p[3]) == int(i_p[1])):
                            self.x = -self.x
                            self.y = -self.y
                            i.hit()
                            if i.hits <= 0:
                                GameObject.all_item.remove(i)
                        elif i_p[0] <= p[2]-self.radius+1 <= i_p[2] and (int(p[3]-1) == int(i_p[1]) or int(p[3]) == int(i_p[1])):
                            self.x = -self.x
                            self.y = -self.y
                            i.hit()
                            if i.hits <= 0:
                                GameObject.all_item.remove(i)

            if len(GameObject.all_item) == 2:
                cls.win_loss(True, True)

            elif not(self.start):
                self.canvas.move(self.ball, self.x, self.y)
                self.canvas.after(self.speed, self.update, bat, cls)

    def collide(self, game_objects):
        return self.list_of_f.append(game_objects)  # ******* useless


class Bat(GameObject):
    def __init__(self, canvas, x, y, width=40, height=12):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.bat = self.canvas.create_rectangle(x - self.width/2, y - self.height/2, x + self.width/2, y + self.height/2
                            , fill="blue")
        self.item = self.bat
        GameObject.all_item.append(self)

    def move(self, x, y):
            p = self.get_position()
            if int(p[0]) <= 12 and x < 0:
                pass
            elif int(p[2]) >= 490 and x > 0:
                pass
            elif int(p[1]) <= 200 and y < 0:
                pass
            elif int(p[3]) >= 320 and y > 0:
                pass
            else:
                self.canvas.move(self.bat, x, y)


class Brick(GameObject):
    def __init__(self, canvas, x, y, hits, color: str = "yellow", width: int = 10, height: int = 10):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.hits = hits
        self.color = color
        if self.hits == 3:
            self.color = "green"
        elif self.hits == 2:
            self.color = "white"
        else:
            self.color = "red"
        self.brick = self.canvas.create_rectangle(x - self.width, y - self.height, x + self.width, y + self.height,
                                                  fill=self.color)
        self.item = self.brick
        GameObject.all_item.append(self)

    def hit(self):
        self.hits -= 1
        if self.hits <= 0:
            self.delete()


class Game:
    def __init__(self):
        self.color = "#f3e6f5"
        self.p1_l = 0
        # ====================================================================================
        # first setting
        self.win = tk.Tk()
        self.win.title("AP4002 Brick Breaker!")
        self.win.resizable(False, False)
        self.win.configure(background=self.color)

        # ====================================================================================
        # add menus
        self.menus = Menu(self.win, background=self.color)
        self.win.config(menu=self.menus, background=self.color)

        self.file_menu = Menu(self.menus, tearoff=0, background=self.color)
        self.file_menu.add_command(label="New", command=self.new_win)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit)

        self.file_menu2 = Menu(self.menus, tearoff=0, background=self.color)
        self.file_menu2.add_command(label="About", command=Game.about)

        self.menus.add_cascade(label="File", menu=self.file_menu, background=self.color)
        self.menus.add_cascade(label="Help", menu=self.file_menu2, background=self.color)

        # ====================================================================================
        # make 3 Frame to work
        self.frame_1 = tk.Frame(self.win, bg=self.color, border=3, relief="groove", highlightthickness=3)
        self.frame_1.grid(column=0, row=0, padx=5, pady=5)
        self.frame_1.focus()

        self.frame_2 = tk.Frame(self.win, bg=self.color, border=3, relief="solid")
        self.frame_2.grid(column=0, row=1, padx=8, pady=5)

        self.frame_3 = tk.Frame(self.win, bg=self.color)
        self.frame_3.grid(column=0, row=2, padx=5, pady=5)
        # re_life = flat, groove, raised, ridge, solid, or sunken

        # ====================================================================================
        # add content to frame 1
        wel_tex = tk.Label(self.frame_1, text="Welcome to Brick Breaker!", bg=self.color)
        wel_tex.grid(column=0, row=0, padx=5, pady=5, columnspan=5)
        sel_tex = tk.Label(self.frame_1, text="Control the Bat and break all Brick", bg=self.color)
        sel_tex.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W, columnspan=5)

        res_tex = tk.Label(self.frame_1, text="Result : ", bg=self.color)
        res_tex.grid(column=0, row=3, padx=5, pady=7, sticky=tk.W)
        res_1_tex = tk.Label(self.frame_1, text="   Loss :", bg=self.color)
        res_1_tex.grid(column=1, row=3, padx=5, pady=7, sticky=tk.W)
        self.P1_res = tk.Label(self.frame_1, text=str(self.p1_l), border=4, relief="ridge", bg=self.color)
        self.P1_res.grid(column=2, row=3, padx=5, pady=7, sticky=tk.W)

        # ====================================================================================
        # add content to frame 2
        self.canvas = tk.Canvas(self.frame_2, width=500, height=320, bg='#ab97de')
        self.canvas.grid(column=0, row=0)
        self.canvas.create_rectangle(-1, 0, 10, 321, fill="#1c1c1c")
        self.canvas.create_rectangle(492, 0, 501, 320, fill="#1c1c1c")
        self.canvas.create_rectangle(-1, 0, 501, 10, fill="#1c1c1c")
        self.ball = Ball(self.canvas, 250, 160, speed=40)

        self.P1 = Bat(self.canvas, 250, 315, width=50)

        for i in range(1, 4):
            for j in range(1, 11):
                globals()[f"self.brick{i}_{j}"] = Brick(self.canvas, j*45, i*30, 4 - i, color="yellow")

        # ====================================================================================
        # add content to frame 3
        self.start_b = tk.Button(self.frame_3, text="Start", command=self.start_pause, font=("Helvetica", 11))
        self.start_b.grid(column=0, row=0, padx=5, pady=5)
        self.state_game = False
        self.start_m = True

        # ====================================================================================
        # start looping
        self.win.mainloop()

    def start_pause(self):
        """start and pause button func"""
        if self.state_game:
            self.state_game = False
            self.start_b.configure(text="Start")

        else:
            self.state_game = True
            self.start_b.configure(text="Pause")
            self.controller()

    def controller(self):
        def move_p1(c):
            if not self.state_game:
                pass
            else:
                if c.keysym == "Up":
                    x, y = 0, -2
                elif c.keysym == "Down":
                    x, y = 0, 2
                elif c.keysym == "Right":
                    x, y = 2, 0
                else:
                    x, y = -2, 0
                self.P1.move(x, y)

        self.canvas.bind_all("<Up>", move_p1)
        self.canvas.bind_all("<Down>", move_p1)
        self.canvas.bind_all("<Right>", move_p1)
        self.canvas.bind_all("<Left>", move_p1)

        self.ball.update(self.P1, self)

    def win_loss(self, st, end):
        self.P1.delete()
        self.ball.delete()

        if end:
            messagebox.showinfo(title="WIN", message="hora \nyou win and game is end.")
            self.win.destroy()
        else:
            self.ball = Ball(self.canvas, 250, 160, speed=40)
            self.P1 = Bat(self.canvas, 250, 315, width=50)
            self.p1_l += 1
            self.P1_res.configure(text=str(self.p1_l))
            self.start_pause()

    def quit(self):
        anw = messagebox.askyesno("Exit warning", "Are you sure you want to exit? \n All progress will be cleared.")
        if anw:
            self.win.quit()
            self.win.destroy()
            exit()

    def new_win(self):
        anw = messagebox.askyesno("Exit warning", "Are you sure you want to start a new window? \n "
                                                  "All progress will be cleared.")
        if anw:
            self.win.destroy()
            os.startfile("pong2.py")

    @staticmethod
    def about():
        messagebox.showinfo(" Info ", " Brick Breaker! \n \n Made by supernova-313 \n"
                                      " Version: 1.0.2  \n Date: 2022-5-1")


if __name__ == '__main__':
    test = Game()

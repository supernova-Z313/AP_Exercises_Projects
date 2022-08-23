import tkinter as tk
from tkinter import Menu, IntVar, ttk, scrolledtext, messagebox
import os
from random import choice

# menus, pause and start, one and two player, counter, frame speed(encrase of speed of game), and more ...
class Pong:
    def __init__(self):
        color = "#f3e6f5"
        # ====================================================================================
        # first setting
        self.win = tk.Tk()
        self.win.title("Pong Game")
        self.win.resizable(False, False)
        self.win.configure(background=color)

        # ====================================================================================
        # add menus
        self.menus = Menu(self.win, background=color)
        self.win.config(menu=self.menus, background=color)

        self.file_menu = Menu(self.menus, tearoff=0, background=color)
        self.file_menu.add_command(label="New", command=self.new_win)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit)

        self.file_menu2 = Menu(self.menus, tearoff=0, background=color)
        self.file_menu2.add_command(label="About", command=Pong.about)

        self.menus.add_cascade(label="File", menu=self.file_menu, background=color)
        self.menus.add_cascade(label="Help", menu=self.file_menu2, background=color)

        # ====================================================================================
        # make 3 Frame to work
        self.frame_1 = tk.Frame(self.win, bg=color, border=3, relief="groove", highlightthickness=3)
        self.frame_1.grid(column=0, row=0, padx=5, pady=5)
        self.frame_1.focus()

        self.frame_2 = tk.Frame(self.win, bg=color, border=3, relief="solid")
        self.frame_2.grid(column=0, row=1, padx=8, pady=5)

        self.frame_3 = tk.Frame(self.win, bg=color)
        self.frame_3.grid(column=0, row=2, padx=5, pady=5)
        # re_life = flat, groove, raised, ridge, solid, or sunken

        # ====================================================================================
        # add content to frame 1
        wel_tex = tk.Label(self.frame_1, text="Welcome to Pong", bg=color)
        wel_tex.grid(column=0, row=0, padx=5, pady=5, columnspan=5)
        sel_tex = tk.Label(self.frame_1, text="Select the game mode before start :                                   \n"
                                              "(in two player, second player should play with W and S)", bg=color)
        sel_tex.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W, columnspan=5)

        self.mode_1 = 1
        self.mode = IntVar()
        self.one = tk.Radiobutton(self.frame_1, text='One player', variable=self.mode, value=1, fg="#5c59ff", bg=color)
        self.one.grid(column=0, row=2, padx=5, pady=5, sticky=tk.W)
        self.one.select()
        self.two = tk.Radiobutton(self.frame_1, text='Two player', variable=self.mode, value=2, fg="#f54275", bg=color)
        self.two.grid(column=1, row=2, padx=5, pady=5, sticky=tk.W)

        res_tex = tk.Label(self.frame_1, text="Result : ", bg=color)
        res_tex.grid(column=0, row=3, padx=5, pady=7, sticky=tk.W)
        res_1_tex = tk.Label(self.frame_1, text="   Player one :", bg=color)
        res_1_tex.grid(column=1, row=3, padx=5, pady=7, sticky=tk.W)
        res_2_tex = tk.Label(self.frame_1, text="   Player two :", bg=color)
        res_2_tex.grid(column=3, row=3, padx=5, pady=7, sticky=tk.W)
        self.P1_res = tk.Label(self.frame_1, text="--", border=4, relief="ridge", bg=color)
        self.P1_res.grid(column=2, row=3, padx=5, pady=7, sticky=tk.W)
        self.P2_res = tk.Label(self.frame_1, text="--", border=4, relief="ridge", bg=color)
        self.P2_res.grid(column=4, row=3, padx=5, pady=7, sticky=tk.W)

        # ====================================================================================
        # add content to frame 2
        self.canvas = tk.Canvas(self.frame_2, width=500, height=320, bg='#ab97de')
        self.canvas.grid(column=0, row=0)
        self.canvas.create_rectangle(-1, 0, 501, 12, fill="#1c1c1c")
        self.canvas.create_rectangle(-1, 310, 501, 320, fill="#1c1c1c")
        # we can use a rectangle but i think if use a line that's better
        # self.canvas.create_rectangle(246, 13, 254, 309, fill="#3d3d3d", outline="#3d3d3d")
        self.canvas.create_line(250, 13, 250, 309, dash=(4, 2))
        self.ball = self.canvas.create_oval(242, 152, 258, 168, fill="yellow")
        self.P2 = self.canvas.create_rectangle(0, 140, 11, 180, fill="blue")
        self.P1 = self.canvas.create_rectangle(490, 140, 500, 180, fill="blue")
        self.P1_s = 0
        self.P2_s = 0
        self.frame_rate = 60
        self.frame_rate_c = 0

        # ====================================================================================
        # add content to frame 3
        self.start_b = tk.Button(self.frame_3, text="Start", command=self.start_pause, font=("Helvetica", 11))
        self.start_b.grid(column=0, row=0, padx=5, pady=5)
        self.state_game = False
        self.start_m = True

        # ====================================================================================
        # start looping
        self.win.mainloop()

    def start_pause(self, mid=False):
        """start and pause button func"""
        if self.state_game:
            self.state_game = False
            self.start_b.configure(text="Start")
            self.one.configure(state="normal")
            self.two.configure(state="normal")

        else:
            self.state_game = True
            self.start_b.configure(text="Pause")
            self.one.configure(state="disabled")
            self.two.configure(state="disabled")
            self.controller()

    def game_counter(self, player):
        """when some one win or loss the game should count that and continue"""
        self.start_pause()
        if player == 1:
            self.P1_s += 1
            if self.P1_s < 10:
                self.P1_res.configure(text=f" {self.P1_s}")
            else:
                self.P1_res.configure(text=str(self.P1_s))
        else:
            self.P2_s += 1
            if self.P2_s < 10:
                self.P2_res.configure(text=f" {self.P2_s}")
            else:
                self.P1_res.configure(text=str(self.P2_s))

        def set_default():
            """ setting the game in first position"""
            self.start_m = True
            self.canvas.delete(self.ball)
            self.ball = self.canvas.create_oval(242, 152, 258, 168, fill="yellow")
            self.canvas.delete(self.P2)
            self.canvas.delete(self.P1)
            self.P2 = self.canvas.create_rectangle(0, 140, 11, 180, fill="blue")
            self.P1 = self.canvas.create_rectangle(490, 140, 500, 180, fill="blue")
            # we can start the game from the base frame but if we use else i think that's better
            # self.frame_rate_c = 0
            self.controller()

        self.canvas.after(1000, set_default)

    def controller(self):
        """ control the version game and play the correct one"""
        self.mode_1 = self.mode.get()
        # one player
        if self.mode_1 == 1:
            self.canvas.focus_set()
            self.player_comp_anime()
            self.player_1_anime()
            self.ball_anime()
        else:  # two player
            self.canvas.focus_set()
            self.player_2_anime()
            self.player_1_anime()
            self.ball_anime()

    def ball_anime(self):
        """ball move system"""
        if self.state_game:  # self.state.game is a var to check the pause or continue game
            # first move is random
            if self.start_m:
                self.x = choice([5, -5])
                self.y = choice([5, -5])
                self.start_m = False
                self.canvas.move(self.ball, self.x, self.y)
            else:
                p1_pos = self.canvas.coords(self.P1)
                p2_pos = self.canvas.coords(self.P2)
                ball_pos = self.canvas.coords(self.ball)

                if 5 <= ball_pos[0] <= 12 and int(ball_pos[1]) >= int(p2_pos[1]-15) and int(ball_pos[1]) <= int(p2_pos[3]):
                    self.x = 5
                    self.canvas.move(self.ball, self.x, self.y)

                elif ball_pos[0] < 5:
                    self.game_counter(1)

                elif 489 <= ball_pos[2] <= 495 and int(ball_pos[3]) >= int(p1_pos[1]) and int(ball_pos[3]) <= int(p1_pos[3]+15):
                    self.x = -5
                    self.canvas.move(self.ball, self.x, self.y)

                elif ball_pos[2] > 495:
                    self.game_counter(2)

                elif ball_pos[1] <= 13:
                    self.y = 5
                    self.canvas.move(self.ball, self.x, self.y)

                elif ball_pos[3] >= 305:
                    self.y = -5
                    self.canvas.move(self.ball, self.x, self.y)

                else:
                    self.canvas.move(self.ball, self.x, self.y)

            # set the frame rate of game or speed of ball
            self.frame_rate_c += 1
            if int(self.frame_rate_c) == 120:
                self.frame_rate = 50
            elif int(self.frame_rate_c) == 320:
                self.frame_rate = 40
            elif int(self.frame_rate_c) == 720:
                self.frame_rate = 30
            elif int(self.frame_rate_c) == 1400:
                self.frame_rate = 20

            # refresh the ball position
            self.canvas.after(self.frame_rate, self.ball_anime)

    def player_1_anime(self):
        """player one move func"""
        def move_p1(event):
            if self.state_game:
                cor = self.canvas.coords(self.P1)
                if event.keysym == "Up":
                    if cor[3] == 307:
                        self.canvas.move(self.P1, 0, -2)
                    elif cor[1] > 15:
                        self.canvas.move(self.P1, 0, -5)
                elif event.keysym == "Down":
                    if cor[3] < 305:
                        self.canvas.move(self.P1, 0, 5)
                    elif cor[3] == 305:
                        self.canvas.move(self.P1, 0, 2)

        # use up and down to control rocket one
        self.canvas.bind("<Up>", move_p1)
        self.canvas.bind("<Down>", move_p1)

    def player_comp_anime(self):
        """AI of player two in one player mode that never loss"""
        def move_p_c(event):
            cor = self.canvas.coords(self.P2)
            if event == "Up":
                if cor[3] == 307:
                    self.canvas.move(self.P2, 0, -2)
                elif cor[1] > 15:
                    self.canvas.move(self.P2, 0, -5)
            elif event == "Down":
                if cor[3] < 305:
                    self.canvas.move(self.P2, 0, 5)
                elif cor[3] == 305:
                    self.canvas.move(self.P2, 0, 2)
        if self.state_game and (self.mode_1 == 1):
            ball_cor = self.canvas.coords(self.ball)
            comp_cor = self.canvas.coords(self.P2)
            if (ball_cor[1]-comp_cor[1]) < 12:
                move_p_c("Up")
            elif (ball_cor[1]-comp_cor[1]) > 12:
                move_p_c("Down")

            # refresh the player two position
            self.canvas.after(self.frame_rate, self.player_comp_anime)

    def player_2_anime(self):
        """player two move func"""
        def move_p2(event):
            if self.state_game:
                cor = self.canvas.coords(self.P2)
                if event.char == "w":
                    if cor[3] == 307:
                        self.canvas.move(self.P2, 0, -2)
                    elif cor[1] > 15:
                        self.canvas.move(self.P2, 0, -5)
                elif event.char == "s":
                    if cor[3] < 305:
                        self.canvas.move(self.P2, 0, 5)
                    elif cor[3] == 305:
                        self.canvas.move(self.P2, 0, 2)

        # use w and s to control rocket two
        self.canvas.bind("<w>", move_p2)
        self.canvas.bind("<s>", move_p2)

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
            os.startfile("pong.py")

    @staticmethod
    def about():
        messagebox.showinfo(" Info ", " PONG Game \n \n Made by supernova-313 \n"
                                      " Version: 1.0.2  \n Date: 2022-3-31")


if __name__ == "__main__":
    game = Pong()

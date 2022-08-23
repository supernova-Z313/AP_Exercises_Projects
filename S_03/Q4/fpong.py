import tkinter as tk
from tkinter import Menu, IntVar, ttk, scrolledtext, messagebox
import os
from random import choice


class Pong:
    def __init__(self):
        color = "#f3e6f5"
        # ====================================================================================
        # first setting
        self.win = tk.Tk()
        self.win.title("F Pong Game")
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
        # self.canvas.create_rectangle(246, 13, 254, 309, fill="#3d3d3d", outline="#3d3d3d")
        self.canvas.create_line(250, 13, 250, 309, dash=(4, 2))
        self.ball = self.canvas.create_oval(242, 152, 258, 168, fill="yellow")
        self.P2 = self.canvas.create_rectangle(0, 140, 11, 180, fill="blue")
        self.P1 = self.canvas.create_rectangle(490, 140, 500, 180, fill="blue")

        # ====================================================================================
        # add content to frame 3
        self.start_b = tk.Button(self.frame_3, text="Start", command=self.start_pause, font=("Helvetica", 11))
        self.start_b.grid(column=0, row=0, padx=5, pady=5)
        self.state_game = False

        # ====================================================================================
        # start looping
        self.win.mainloop()

    def start_pause(self):
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

    def controller(self):
        self.mode_1 = self.mode.get()
        if self.mode_1 == 1:
            self.canvas.focus_set()
            self.player_comp_anime()
            self.player_1_anime()
            self.ball_anime()
        else:
            self.canvas.focus_set()
            self.player_2_anime()
            self.player_1_anime()
            self.ball_anime()

    def ball_anime(self):
        start = True
        if self.state_game:
            self.canvas.after(100, self.ball_anime)
            if start:
                x = choice([5, -5])
                y = choice([5, -5])
                start = False
                self.canvas.move(self.ball, x, y)
            else:
                pass

    def player_1_anime(self):
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

        self.canvas.bind("<Up>", move_p1)
        self.canvas.bind("<Down>", move_p1)

    def player_comp_anime(self):
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
            self.canvas.after(100, self.player_comp_anime)

    def player_2_anime(self):
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

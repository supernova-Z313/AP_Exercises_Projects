from tkinter import Menu, IntVar, ttk, messagebox
import tkinter as tk
import time
import os
# ==========================================================================================
"""
gabeliat haye ezafe : menu , tab , dark and light mode , information , tatal time , start button , play agian game , button color , restart game , turn , result and other ...
"""
coler = "#f3e6f5"

# ==========================================================================================

def quit():
    def warning_Exit():
        global anw
        anw = messagebox.askyesno("Exit warning", "Are you sure you want to exit? \n All progress will be cleared.")
    warning_Exit()
    if anw == True:
        win.quit()
        win.destroy()
        exit()

# ==========================================================================================

def New_win():
    def warning_Exit():
        global anw
        anw = messagebox.askyesno("Exit warning", "Are you sure you want to start a new window? \n All progress will be cleared.")
    warning_Exit()

    if anw == True:
        def restart():
            win.destroy()
            os.startfile("t2.py")
        restart()

# ==========================================================================================

def about():
    messagebox.showinfo(" Info ", " TIC TAC TOE \n \n Made by supernova-313 \n Version: 1.0.0 (system setup) \n Date: 2022-2-26")

# ==========================================================================================

def update():
    messagebox.showerror(" nop ", "become a enjoyer bro \U0001F4AA \ndon't be a updata fans")

# ==========================================================================================


win = tk.Tk()
win.title("tic tac toe")
win.resizable(False, False)
win.configure(background=coler)
menus = Menu(win, background=coler)
win.config(menu=menus,background=coler)

file_menu = Menu(menus, tearoff = 0,background=coler)
file_menu.add_command(label="New", command = New_win)
file_menu.add_separator()
file_menu.add_command(label="Exit", command = quit)

file_menu2 = Menu(menus, tearoff = 0, background=coler)
file_menu2.add_command(label="About", command= about)

menus.add_cascade(label="File", menu=file_menu,background=coler)
menus.add_cascade(label="Help", menu=file_menu2,background=coler)

tabControl = ttk.Notebook(win)
tab1 = tk.Frame(tabControl,background=coler)
tab2 = tk.Frame(tabControl,background=coler)
tabControl.add(tab1, text=' game ')
tabControl.add(tab2, text=' settings ')
tabControl.pack(expand=1, fill="both")

# =============================================================================================
# tab1
frame2 = tk.Frame(tab1, border = 3,relief="groove", highlightthickness=2)
frame2.grid(column = 0, row = 0, padx= 7 , pady= 3, sticky=tk.N)
frame2.configure(background=coler)

titr = ttk.Label(frame2, text="Information : \nthis is the tic tac to game, game start with a square that have 9 cell, in each round\nplayer should select a cell to change the status of that cell to player mark . there is\ntwo mark \"X\" and \"O\" and game will start with mark \"X\" \nfor start the game click the button : ",background=coler)
titr.grid(column=0, row=0, sticky= tk.W, pady=5, padx=1)

XT = 0
OT = 0

def main_def():
    global nobat, frame3, XT, OT
    info_b.destroy()
    
    titr.configure(text=f" POINTS (X,O): {XT}  /  {OT}\n SHIFT : X")
    start = time.time()

    frame3 = tk.Frame(tab1, border=3)
    frame3.grid(column = 0, row = 1, rowspan=2, padx= 7 , pady= 2)
    frame3.configure(background=coler)

    listkol = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
    nobat = 1
    
    colcall()

    def disableb(a,b):
        global XT, OT
        for i in cells:
            i.configure(state="disabled")
        end = time.time()
        alltime = int(end-start)
        if a == 0:
            anw = messagebox.askyesno("Tic Tac Toe", f"It's a tie!!\nNo one wins!Reset the game...\ntotal time : {alltime} s\nif you want to play again click yes and for exit clik no.")
            if anw == True:
                # win.destroy()
                # os.startfile("t2.py")
                main_def()
            else:
                win.quit()
                win.destroy()
                exit()
        else:
            if b == 1:
                t = "first team(X)"
                XT += 1
            else:
                t = "second team(O)"
                OT += 1
            anw = messagebox.askyesno("Tic Tac Toe",f"the {t} is win!\ntotal time : {alltime} s\nif you want to play again click yes and for exit clik no.")
            if anw == True:
                # win.destroy()
                # os.startfile("t2.py")
                main_def()
            else:
                win.quit()
                win.destroy()
                exit()

    def checkall():
        colcall()
        if nobat % 2 == 1:
            namee = "X"
        else:
            namee = "O"
        titr.configure(text=f" POINTS (X,O): {XT}  /  {OT}\n SHIFT : {namee}")

        for i in listkol:
            if i == [1, 1, 1] or i == [2, 2, 2]:
                disableb(1,i[0])
        for index, i in enumerate(listkol[0]):
            if (i == listkol[1][index]) and (i == listkol[2][index]) and (i != 0):
                disableb(1, i)
        if (listkol[0][0] == listkol[1][1]) and (listkol[0][0] == listkol[2][2]) and (listkol[0][0] != 0):
            disableb(1, listkol[0][0])
        if (listkol[0][2] == listkol[1][1]) and (listkol[0][2] == listkol[2][0]) and (listkol[0][2] != 0):
            disableb(1, listkol[0][2])
        counter = 0
        for i in listkol:
            for j in i:
                if j == 0:
                    counter += 1
        if counter == 0:
            disableb(0, 0)

    def bc1():
        global nobat
        if nobat%2 == 1:
            b1.configure(text="X",state="disabled", bg="#f25b50")
            nobat += 1
            listkol[0][0] = 1
            checkall()
        else:
            b1.configure(text="O",state="disabled", bg="#5086f2")
            nobat += 1
            listkol[0][0] = 2
            checkall()
    
    def bc2():
        global nobat
        if nobat%2 == 1:
            b2.configure(text="X",state="disabled", bg="#f25b50")
            nobat += 1
            listkol[0][1] = 1
            checkall()
        else:
            b2.configure(text="O",state="disabled", bg="#5086f2")
            nobat += 1
            listkol[0][1] = 2
            checkall()

    def bc3():
        global nobat
        if nobat%2 == 1:
            b3.configure(text="X",state="disabled", bg="#f25b50")
            nobat += 1
            listkol[0][2] = 1
            checkall()
        else:
            b3.configure(text="O",state="disabled", bg="#5086f2")
            nobat += 1
            listkol[0][2] = 2
            checkall()

    def bc4():
        global nobat
        if nobat%2 == 1:
            b4.configure(text="X",state="disabled", bg="#f25b50")
            nobat += 1
            listkol[1][0] = 1
            checkall()
        else:
            b4.configure(text="O",state="disabled", bg="#5086f2")
            nobat += 1
            listkol[1][0] = 2
            checkall()

    def bc5():
        global nobat
        if nobat%2 == 1:
            b5.configure(text="X",state="disabled", bg="#f25b50")
            nobat += 1
            listkol[1][1] = 1
            checkall()
        else:
            b5.configure(text="O",state="disabled", bg="#5086f2")
            nobat += 1
            listkol[1][1] = 2
            checkall()

    def bc6():
        global nobat
        if nobat%2 == 1:
            b6.configure(text="X",state="disabled", bg="#f25b50")
            nobat += 1
            listkol[1][2] = 1
            checkall()
        else:
            b6.configure(text="O",state="disabled", bg="#5086f2")
            nobat += 1
            listkol[1][2] = 2
            checkall()

    def bc7():
        global nobat
        if nobat%2 == 1:
            b7.configure(text="X",state="disabled", bg="#f25b50")
            nobat += 1
            listkol[2][0] = 1
            checkall()
        else:
            b7.configure(text="O",state="disabled", bg="#5086f2")
            nobat += 1
            listkol[2][0] = 2
            checkall()

    def bc8():
        global nobat
        if nobat%2 == 1:
            b8.configure(text="X",state="disabled", bg="#f25b50")
            nobat += 1
            listkol[2][1] = 1
            checkall()
        else:
            b8.configure(text="O",state="disabled", bg="#5086f2")
            nobat += 1
            listkol[2][1] = 2
            checkall()

    def bc9():
        global nobat
        if nobat%2 == 1:
            b9.configure(text="X",state="disabled", bg="#f25b50")
            nobat += 1
            listkol[2][2] = 1
            checkall()
        else:
            b9.configure(text="O",state="disabled", bg="#5086f2")
            nobat += 1
            listkol[2][2] = 2
            checkall()


    b1 = tk.Button(frame3, text="  ",command=bc1, font=("Helvetica", 20), height=1, width=3)
    b1.grid(column=0, row=0, padx=2,pady=2)

    b2 = tk.Button(frame3, text="  ",command=bc2, font=("Helvetica", 20), height=1, width=3)
    b2.grid(column=1, row=0, padx=2,pady=2)

    b3 = tk.Button(frame3, text="  ",command=bc3, font=("Helvetica", 20), height=1, width=3)
    b3.grid(column=2, row=0, padx=2,pady=2)
    
    b4 = tk.Button(frame3, text="  ",command=bc4, font=("Helvetica", 20), height=1, width=3)
    b4.grid(column=0, row=1, padx=2,pady=2)
    
    b5 = tk.Button(frame3, text="  ", font=("Helvetica", 20), height=1, width=3,command=bc5)
    b5.grid(column=1, row=1, padx=2,pady=2)
    
    b6 = tk.Button(frame3, text="  ", font=("Helvetica", 20), height=1, width=3,command=bc6)
    b6.grid(column=2, row=1, padx=2,pady=2)
    
    b7 = tk.Button(frame3, text="  ", font=("Helvetica", 20), height=1, width=3,command=bc7)
    b7.grid(column=0, row=2, padx=2,pady=2)
    
    b8 = tk.Button(frame3, text="  ", font=("Helvetica", 20), height=1, width=3,command=bc8)
    b8.grid(column=1, row=2, padx=2,pady=2)
    
    b9 = tk.Button(frame3, text="  ", font=("Helvetica", 20), height=1, width=3,command=bc9)
    b9.grid(column=2, row=2, padx=2,pady=2)

    cells = [b1,b2,b3,b4,b5,b6,b7,b8,b9]

info_b = ttk.Button(frame2, text="next", command= main_def)
info_b.grid(column=0, row=1, sticky= tk.E, pady=5, padx=5)

# ==========================================================================================
# tab2
mode = tk.Frame(tab2, border=7,relief="sunken", highlightthickness=2)
mode.grid(column=0, row=0, padx= 7, pady= 7)
mode.configure(background=coler)

mode_text = ttk.Label(mode, text="Mode:", font=("Courier", 10))
mode_text.grid(column=0,row=0, padx=7,pady=7, sticky= tk.W)
mode_text.configure(background=coler)


def colcall():
    global frame3
    v_volor = color_b.get()
    if v_volor == 1:
        col1.configure(background="#343645",fg="#5c59ff")
        col2.configure(background="#343645",fg="#e09538")# #ffff40
        mode_text.configure(background="#343645",foreground="#b84040")
        mode.configure(background="#343645")
        tab1.configure(background="#121340")
        tab2.configure(background="#121340")
        file_menu.configure(background="#121340",foreground="#dfdfed")
        file_menu2.configure(background="#121340",foreground="#dfdfed")
        win.configure(background="#343645")
        frame2.configure(background="#343645")
        titr.configure(background="#343645",foreground="#e09538")
        staylwin.configure('TNotebook.Tab', background="#121340",foreground="#dfdfed")
        try:
            frame3.configure(background="#121340")
        except:
            pass
    elif v_volor == 2:
        col1.configure(background="#dfdfed",fg="#5c59ff")
        col2.configure(background="#dfdfed",fg="#e09538")
        mode_text.configure(background="#dfdfed",foreground="#b84040")
        mode.configure(background="#dfdfed")
        tab1.configure(background="#f0f0f0")
        tab2.configure(background="#f0f0f0")
        file_menu.configure(background="#dfdfed",foreground="#171717")
        file_menu2.configure(background="#dfdfed",foreground="#171717")
        win.configure(background="#dfdfed")
        frame2.configure(background="#dfdfed")
        titr.configure(background="#dfdfed",foreground="#5c59ff")
        staylwin.configure('TNotebook.Tab', background="#f0f0f0",foreground="#171717")
        try:
            frame3.configure(background="#dfdfed")
        except:
            pass
    else:
        pass



color_b = IntVar()
col1 = tk.Radiobutton(mode, text = 'Dark_Blue', variable = color_b, value = 1,fg="#5c59ff", command= colcall)#  , command = colcall
col1.grid(column = 0, row = 1,padx= 4 , pady= 4, sticky = tk.W)
col1.configure(background=coler)
col2 = tk.Radiobutton(mode, text="Light", variable= color_b, value= 2,fg="#e09538", command= colcall)
col2.grid(column = 1, row = 1,padx= 4 , pady= 4, sticky = tk.W)
col2.configure(background=coler)


# =============================================================================================

staylwin = ttk.Style()
# staylwin.theme_use('winnative')
staylwin.configure('TNotebook.Tab', background=coler)

win.mainloop()

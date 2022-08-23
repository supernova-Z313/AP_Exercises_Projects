import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import threading
import bs4
import requests


win = tk.Tk()
win.title("q2")
win.geometry("700x600")
win.resizable(False, False)


def search_1():
    global words, counter
    search.config(text="search more")
    w = word.get()
    if w == words:
        counter += 4
    thread1 = threading.Thread(target=searching)
    thread1.start()


def searching():
    global counter, links, words, pic_counter
    words = word.get()
    words = words.replace(" ", "%20")
    res = requests.get(f"https://www.bing.com/images/async?q={words}&first=0&count={counter}&cw=1177&ch=696&relp=35&"
                       "tsc=ImageHoverTitle&datsrc=I&layout=RowBased&mmasync=1",
                       headers={'Host': 'www.bing.com', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
                                'Accept-Language': 'en-US,en;q=0.5', 'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1',
                                'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'none',
                                'Sec-Fetch-User': '?1', 'Pragma': 'no-cache', 'Cache-Control': 'no-cache'}, stream=True)
    soup = bs4.BeautifulSoup(res.content, "html5lib")
    images = soup.find_all("a", attrs={"class": "iusc"})

    for i in images:
        link = eval(i["m"])["murl"]
        if link not in links:
            links.append(link)

    for ind, i in enumerate(links[-1:-11:-1]):
        try:
            img = requests.get(i, timeout=10)  # , stream=True
            print(img)
            if img.status_code == 200:
                t.config(state="normal")
                try:
                    open(f"pic_{ind}.jpg", "wb").write(img.content)
                    globals()[f"img{pic_counter}"] = Image.open(f'pic_{ind}.jpg').resize((300, 205))
                    globals()[f"img{pic_counter}"] = ImageTk.PhotoImage(globals()[f"img{pic_counter}"])
                    t.window_create(tk.END, window=tk.Label(t, image=globals()[f"img{pic_counter}"]))
                    pic_counter += 1
                    if pic_counter % 2 == 0:
                        t.insert(tk.END, "\n")
                    os.remove(f"pic_{ind}.jpg")
                except:
                    os.remove(f"pic_{ind}.jpg")
                    try:
                        open(f"pic_{ind}.jpeg", "wb").write(img.content)
                        globals()[f"img{pic_counter}"] = Image.open(f"pic_{ind}.jpeg").resize((300, 205))
                        globals()[f"img{pic_counter}"] = ImageTk.PhotoImage(globals()[f"img{pic_counter}"])
                        t.window_create(tk.END, window=tk.Label(t, image=globals()[f"img{pic_counter}"]))
                        pic_counter += 1
                        if pic_counter % 2 == 0:
                            t.insert(tk.END, "\n")
                        os.remove(f"pic_{ind}.jpeg")
                    except:
                        os.remove(f"pic_{ind}.jpeg")
                        try:
                            open(f"pic_{ind}.png", "wb").write(img.content)
                            globals()[f"img{pic_counter}"] = Image.open(f"pic_{ind}.png").resize((300, 205))
                            globals()[f"img{pic_counter}"] = tk.PhotoImage(file=f'pic_{ind}.png')
                            t.window_create(tk.END, window=tk.Label(t, image=globals()[f"img{pic_counter}"]))
                            pic_counter += 1
                            if pic_counter % 2 == 0:
                                t.insert(tk.END, "\n")
                            os.remove(f"pic_{ind}.png")
                        except:
                            print("picture failed on load")
                            os.remove(f"pic_{ind}.png")
                t.config(state="disabled")
        except:
            print("network failed")


def clear_1():
    global counter
    search.config(text="search")
    counter = 10
    t.config(state="normal")
    t.delete(1.0, tk.END)
    t.config(state="disabled")


def closing():
    win.destroy()


frame1 = ttk.LabelFrame(win, text="title")
frame1.grid(row=0, column=0, pady=5, padx=5)

f_text = tk.Label(frame1, text="please enter the text for search :             ")
f_text.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

pic_counter = 0
words = " "
links = []
counter = 10
word = tk.StringVar()
word_box = tk.Entry(frame1, width=20, textvariable=word)
word_box.grid(row=0, column=1, pady=5, padx=5, sticky=tk.E)

search = tk.Button(frame1, text="search", command=search_1)
search.grid(row=1, column=0, pady=5, padx=5, sticky=tk.W)

clear = tk.Button(frame1, text="clear the Box", command=clear_1)
clear.grid(row=1, column=1, padx=5, pady=5, sticky=tk.E)

close = tk.Button(frame1, text="close the app ED", command=closing)
close.grid(row=2, column=0, columnspan=2, pady=5, padx=5)

frame2 = ttk.LabelFrame(win, text="result")
frame2.grid(row=1, column=0, pady=5, padx=5)


h = tk.Scrollbar(frame2, orient='horizontal')
h.pack(side=tk.BOTTOM, fill=tk.X)
v = tk.Scrollbar(frame2)
v.pack(side=tk.RIGHT, fill=tk.Y)
t = tk.Text(frame2, width=83, height=23, wrap=tk.NONE, xscrollcommand=h.set, yscrollcommand=v.set)
t.pack(side=tk.TOP, fill=tk.X)
t.config(state="disabled")
h.config(command=t.xview)
v.config(command=t.yview)

# img = tk.PhotoImage(file='good.png')
# # t.image_create(tk.END, image=img)
# t.window_create(tk.END, window=tk.Label(t, image=img))

win.mainloop()

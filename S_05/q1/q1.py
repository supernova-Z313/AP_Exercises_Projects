import tkinter as tk
from tkinter import ttk
import threading
import bs4
import requests
import re
from functools import partial


class HyperlinkManager:
    def __init__(self, text):
        self.text = text
        self.text.tag_config("hyper", foreground="blue", underline=1)
        self.text.tag_bind("hyper", "<Enter>", self._enter)
        self.text.tag_bind("hyper", "<Leave>", self._leave)
        self.text.tag_bind("hyper", "<Button-1>", self._click)
        self.reset()

    def reset(self):
        self.links = {}

    def add(self, action):
        # add an action to the manager.  returns tags to use in
        # associated text widget
        tag = "hyper-%d" % len(self.links)
        self.links[tag] = action
        return "hyper", tag

    def _enter(self, event):
        self.text.config(cursor="hand2")

    def _leave(self, event):
        self.text.config(cursor="")

    def _click(self, event):
        for tag in self.text.tag_names(tk.CURRENT):
            if tag[:6] == "hyper-":
                self.links[tag]()
                return


win = tk.Tk()
win.geometry("550x550")
win.resizable(False, False)
win.title("q1")


def clearing():
    text_widget.config(state="normal")
    text_widget.delete(1.0, tk.END)
    text_widget.config(state="disabled")


def clearing_1():
    job_ch.config(state="normal")
    search.config(state="normal")
    clearing()


def work_info_1(link, name):
    thread3 = threading.Thread(target=work_info, args={link, name})
    thread3.start()


def work_info(link: str, name: str):
    job_ch.config(state="disabled")
    search.config(state="disabled")
    f_text.config(text="for select another job clear the box and search again.     ")
    clearing()
    res3 = requests.get(link)
    doc3 = bs4.BeautifulSoup(res3.content, "html5lib")
    t2 = doc3.find("p", attrs={"class": "attrgroup"})
    inf = re.findall("<span>\n  (.*):\n  <b>\n   (.*)\n  </b>", t2.prettify())
    t3 = doc3.find("section", attrs={"id": "postingbody"})
    mat = t3.text
    mat = mat.replace("QR Code Link to This Post", " ")
    mat = mat.lstrip()
    text_widget.config(state="normal")
    text_widget.insert(tk.END, name+"\n\n")
    text_widget.insert(tk.END, "====================<important information>====================\n")
    for i in inf:
        text_widget.insert(tk.END, i[0]+" : "+i[1]+"\n")
    text_widget.insert(tk.END, "===============================================================\n\n")
    text_widget.insert(tk.END, mat)
    text_widget.config(state="disabled")


def searching_1():
    thread2 = threading.Thread(target=searching)
    thread2.start()


def searching():
    global job_names, jobs_url
    f_text.config(text="please select a job to see that information.                      ")
    t_job = job.get()
    n = job_names.index(t_job)
    url = "https://boston.craigslist.org/search/" + jobs_url[n]
    res2 = requests.get(url)
    doc2 = bs4.BeautifulSoup(res2.content, "html5lib")
    jobs_list = doc2.find_all("a", attrs={"class": "result-title hdrlnk"})
    jobs_dict = {}
    for i in jobs_list:
        jobs_dict[re.findall("\">(.*)</a>", str(i))[0]] = re.findall("href=\"(.*)\" id", str(i))[0]
    text_widget.config(state="normal")
    for ind, i in enumerate(jobs_dict):
        text_widget.insert(tk.END, i+"\n", hyperlink.add(partial(work_info_1, jobs_dict[i], i)))
        text_widget.insert(tk.END, "+-----------------------------<=>-----------------------------+\n")
    text_widget.config(state="disabled")
    clear.config(state="normal")


def first_link():
    global job_names, jobs_url
    try:
        res = requests.get("https://boston.craigslist.org/search/jjj?")
        document = bs4.BeautifulSoup(res.content, 'html5lib')
        table = document.find('select', attrs={"id": "subcatAbb"})
        job_names = table.text.split("\n")
        job_names = job_names[1: -1]
        job_names = list(x.lstrip() for x in job_names)
        jobs_url = re.findall("<option value=\"(.*)\">", table.prettify())
        job_ch["values"] = job_names
        job_ch.current(1)
        f_text.config(text="please select a job and click search                                  ")
        search.config(state="normal")
    except:
        print("network failed")


frame1 = ttk.LabelFrame(win, text="title")
frame1.grid(row=0, column=0, pady=5, padx=5)

f_text = ttk.Label(frame1, text="we trying to get information from web, pleas wait.          ")
f_text.grid(row=0, column=0, padx=7, pady=7)

job = tk.StringVar()
job_ch = ttk.Combobox(frame1, width=10, textvariable=job, state="readonly", values=[])
job_ch.grid(row=0, column=1, padx=5, pady=5, sticky=tk.E)

search = ttk.Button(frame1, text="search", command=searching_1, state="disabled")
search.grid(row=1, column=0, pady=7, padx=7, sticky=tk.W)

clear = ttk.Button(frame1, text="clear the result Box", command=clearing_1, state="disabled")
clear.grid(row=1, column=1, padx=5, pady=7, sticky=tk.E)

frame2 = ttk.LabelFrame(win, text="result")
frame2.grid(row=1, column=0, pady=5, padx=5)

text_widget = tk.Text(frame2, height=23, width=63, state="disabled", wrap="word")
text_widget.pack(side=tk.LEFT, pady=5, padx=5, expand=True)
hyperlink = HyperlinkManager(text_widget)


scroll_bar = tk.Scrollbar(frame2)
scroll_bar.pack(side=tk.RIGHT, fill=tk.BOTH)
text_widget.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=text_widget.yview)

win.update()
thread1 = threading.Thread(target=first_link)
thread1.start()

win.mainloop()

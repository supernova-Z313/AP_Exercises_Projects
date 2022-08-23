import tkinter
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.font import Font
from tkinter.scrolledtext import *
import file_menu
import edit_menu
import format_menu
import help_menu
import time
import threading
import multiprocessing
# ================================================================

all_meaning_words = {}
with open("words.txt", "r") as f:
    for i in f.readlines():
        all_meaning_words[i[:-1]] = 0

# ================================================================
root = Tk()
root.title("Text Editor-Untiltled")
root.geometry("300x250+300+300")
root.minsize(width=400, height=400)
# ================================================================
menubar = Menu(root)
mymenu = Menu(root)
mymenu.add_command(label="mycommand", command=print)
# ================================================================

text = ScrolledText(root, state='normal', height=400, width=400, wrap='word', pady=2, padx=3, undo=True)
text.pack(fill=Y, expand=1)
running = True
text.focus_set()
all_word = []


def char_g():
    global all_word
    last_word = ""
    word_char_counter = 2
    while running:
        time.sleep(0.05)
        t = text.get(f"end -{word_char_counter} chars", "end -1 chars")

        if t != " " and len(t) > 0:
            if len(t) > len(last_word) and t[0] != " ":
                word_char_counter += 1
                last_word = t
            if len(t) >= 3:
                if len(t) == len(last_word) and t[1] == " ":
                    word_char_counter -= 1
                    last_word = last_word[1:]

            if len(t) >= 1 and (t[-1] == " "):  # or t[-1] == "\n"
                if last_word != " ":
                    all_word.append(last_word.strip())
                    word_char_counter = 2
                    last_word = ""

    th1.join()


th1 = threading.Thread(target=char_g)
th1.start()


def proces():
    global all_word
    word_index = 0
    children = multiprocessing.Value("i", 1)
    word_processed = multiprocessing.Value("i", 0)
    number_of_core = multiprocessing.cpu_count()

    def word_finder(word: str, index: int, arg=None, args=None):
        res = [word]
        if word == word[::-1]:
            res.append(f"the word {word} is palindrome")
        else:
            res.append(f"the word {word} is not palindrome")

        if word in all_meaning_words:
            res.append(f"the word {word} is meaningful")
        else:
            res.append(f"the word {word} is not meaningful")

        if word[::-1] in all_meaning_words:
            res.append(f"reverse of word {word} is meaningful")
        else:
            res.append(f"reverse of word {word} is not meaningful")

        if len(word) >= 4:
            for ind in range(2, len(word)):
                if word[0:ind] == word[ind-1::-1] and word[ind:] == word[-1:ind-1:-1]:
                    res.append(f"the word {word} is two_word_palindrome")
                    break
            if len(res) == 4:
                res.append(f"the word {word} is not two_word_palindrome")
        else:
            res.append(f"the word {word} is not two_word_palindrome")

        res.append("==================================================")
        while args.value < index-1:
            time.sleep(0.2)
        for j in res:
            print(j)

        if args:
            args.value += 1
        if arg:
            arg.value -= 1

    while running:
        time.sleep(0.025)
        for gg in all_word:
            if children.value < number_of_core-1:
                children.value += 1
                word_index += 1
                multiprocessing.Process(target=word_finder, args=(gg, word_index, children, word_processed)).start()

            else:
                time.sleep(0.5)
                word_index += 1
                threading.Thread(target=word_finder, args=(gg, word_index, None, word_processed)).start()

            all_word.remove(gg)


th2 = threading.Thread(target=proces)
th2.start()

# ================================================================
file_menu.main(root, text, menubar)
edit_menu.main(root, text, menubar)
format_menu.main(root, text, menubar)
help_menu.main(root, text, menubar)
root.mainloop()
running = False

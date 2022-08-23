import tkinter

import requests
import bs4
import re


# inp = input()
# inp = inp.replace(" ", "%20")

# link = "https://www.bing.com/images/search?q=" + "pizza"
# print(link)
# res = requests.get(link)
# print(res)
# print(res.text)
# soup = bs4.BeautifulSoup(res.content, "html5lib")
# soup_1 = soup.find_all("img")
#
# for i in soup_1:
#     try:
#         print(i["src"])
#     except:
#         pass

# img2 = "https://th.bing.com/th/id/OIP.DQgrHFjN_6B7kPFqhnuSOwHaEK?w=317&h=180&c=7&r=0&o=5&pid=1.7"
# res4 = requests.get(img2, stream=True).content
# open("testro.jpg", "wb").write(res4)
# print(res4)
#
# img_2 = "https://th.bing.com/th/id/OIP.DQgrHFjN_emb82E8DDD9B"
# res2 = requests.get(img_2, stream=True)
# open("heeee.png", "wb").write(res2.content)
# print(res2.content)


# jpg = "http://howtoeat.ca/wp-content/uploads/2019/07/IMG_7928.jpg"
# #
#
# jpeg = "https://tse2.mm.bing.net/th?id=OIP.CsCxKLgElKLPm9VcuMCF2AHaKD&amp;pid=15.1"
# #
#
#
# print(requests.get(jpg, timeout=0.5).content[0:50])
# print("fff")
# print(requests.get(jpeg).content[0:50])

# res = requests.get("https://www.bing.com/images/async?q=pizza&first=0&count=10&cw=1177&ch=696&relp=35&"
#                    "tsc=ImageHoverTitle&datsrc=I&layout=RowBased&mmasync=1",
#                     headers={'Host': 'www.bing.com', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
#                              'Accept-Language': 'en-US,en;q=0.5', 'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1',
#                              'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'none',
#                              'Sec-Fetch-User': '?1', 'Pragma': 'no-cache', 'Cache-Control': 'no-cache'}, stream=True)
# soupe = bs4.BeautifulSoup(res.content, "html5lib")
# lin = soupe.find_all("a", attrs={"class": "iusc"})
# for i in lin:
#     x = i["m"]
#     y = eval(x)
#     print(y["murl"])
# for ind, i in enumerate(lin):
#     print(i)
#     try:
#         resw = requests.get(i.img.get("src"))
#         open(f"{ind}_1.jpg", "wb").write(resw.content)
#     except:
#         print("ffff")

# print(res.text)
win = tkinter.Tk()
res = requests.get('https://media.geeksforgeeks.org/wp-content/uploads/20210318103632/gfg-300x300.png')
open("fff.png", "wb").write(res.content)
img = tkinter.PhotoImage(file="fff.png")
win.mainloop()
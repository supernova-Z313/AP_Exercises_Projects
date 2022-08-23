
import requests
import bs4
import re

res = requests.get("https://boston.craigslist.org/search/jjj?")
document = bs4.BeautifulSoup(res.content, 'html5lib')
table = document.find('select', attrs={"id": "subcatAbb"})
print(res)
txt = table.text
txt = txt.split()
print(txt)
jobs = re.findall("<option value=\"(.*)\">", table.prettify())
print(jobs)

g = document.find_all("a", attrs={"class": "result-title hdrlnk"})
print(g)
fuck = {}
for i in g:
    fuck[re.findall("\">(.*)</a>", str(i))[0]] = re.findall("href=\"(.*)\" id", str(i))[0]
print(fuck)
print(len(fuck))

res2 = requests.get('https://boston.craigslist.org/nwb/trp/d/east-boston-truck-driver-wanted-pay/7492479422.html')
print(res2)
doc2 = bs4.BeautifulSoup(res2.content, "html5lib")
t2 = doc2.find("p", attrs={"class": "attrgroup"})
inf = re.findall("<span>\n  (.*):\n  <b>\n   (.*)\n  </b>", t2.prettify())
print(inf)
t3 = doc2.find("section", attrs={"id": "postingbody"})
mat = t3.text
mat = mat.replace("QR Code Link to This Post", " ")
mat = mat.lstrip()
print(mat)


# import requests
#
# url = "https://bama.ir"
# payload = {"UrlBox": url, "AgentList": "Mozilla Firefox", "VersionsList": "HTTP/1.1", "MethodList": "GET"}
# res = requests.get(url="https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", data=payload).status_code
# print(res)
# print(res.text())

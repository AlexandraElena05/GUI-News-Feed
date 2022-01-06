import requests
import tkinter as tk
from tkinter import *
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
from tkinter import font
import re
import html2text

def getNews():
    api_key = "c89a0fdb7dc24da8ba6cbc15c6152dad"
    url = "https://newsapi.org/v2/everything?domains=cnn.com,telegraph.co.uk,bbc.com,reddit.com&language=en&sortBy=publishedAt&apiKey=" + api_key
    news = requests.get(url).json()
    page = urlopen(url)

    html_text = page.read()
    html = html_text.decode("utf-8")
    rendered_content = html2text.html2text(html)

    class Article:
        title = ""
        content = ""
        def __init__(self,title,content):
            self.title=title
            self.content=content


    articles = news["articles"]

    my_articles = []
    my_content = []
    my_news = ""
    searched_topic = "Biden"
    for article in articles:
        if(article["content"].find(searched_topic)!=-1):
            my_articles.append(Article(article["title"], article["content"]))

    for i in range(len(my_articles)):
        my_news = my_news + my_articles[i].title + "=>" + my_articles[i].content + "\n"

    label.config(text=my_news)

canvas = tk.Tk()
canvas.geometry("900x600")
canvas.title("GUI News Feed")
label = tk.Message()

menu = tk.Menu(canvas)
canvas.config(menu=menu)
file_menu = tk.Menu(menu)

file_menu = tk.Menu(
    menu,
    tearoff=0
)

file_menu.add_command(
    label='Exit',
    command=canvas.destroy,
)

menu.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)

help_menu = tk.Menu(
    menu,
    tearoff=0
)

help_menu.add_command(label='Welcome')
help_menu.add_command(label='About...')

menu.add_cascade(
    label="Help",
    menu=help_menu
)

def myClick():
    getNews()
    myLabel = tk.Label(canvas, font=18, text="Now the news are refreshed!")
    myLabel.pack()

button = tk.Button(canvas, font=24, text="Reload", command=myClick)
button.pack(pady=20)

label = tk.Label(canvas, font=18, justify="left")
label.pack(pady=20)

getNews()

canvas.mainloop()

import requests
import tkinter as tk
from tkinter import *


def getNews():
    api_key = "c89a0fdb7dc24da8ba6cbc15c6152dad"
    url = "https://newsapi.org/v2/everything?domains=cnn.com,telegraph.co.uk,bbc.com,reddit.com&language=en&sortBy=publishedAt&apiKey=" + api_key
    news = requests.get(url).json()

    class Article:
        title = ""
        content = ""

        def __init__(self, title, content):
            self.title = title
            self.content = content

    articles = news["articles"]

    my_articles = []
    my_news = ""

    def search():
        searched_topics = enter_box.get()
        return searched_topics

    label1 = tk.Label(canvas, text = "Enter your search here", font = 15)
    label1.grid(row=0, column=0)
    enter_box = tk.Entry(canvas, width = 35)
    enter_box.grid(row=0, column=1)
    btn = tk.Button(canvas, text = "Search", command = search, bg = "blue")
    btn.grid(row=1, column=0)

    searched_topic = search()

    for article in articles:
        if(article["content"].find(searched_topic)!=-1):
            my_articles.append(Article(article["title"], article["content"]))

    for i in range(len(my_articles)):
        my_news = my_news + my_articles[i].title + "=>" + my_articles[i].content + "\n"

    label.config(text=my_news, wraplength=550)


canvas = tk.Tk()
canvas.geometry("900x600")
canvas.title("GUI News Feed")
label = tk.Label()

scrollbar = tk.Scrollbar(canvas)
scrollbar.pack(side=RIGHT, fill=Y)

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

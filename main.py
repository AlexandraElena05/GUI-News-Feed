import requests
import tkinter as tk

def getNews():
    api_key = "c89a0fdb7dc24da8ba6cbc15c6152dad"
    url = "https://newsapi.org/v2/everything?domains=cnn.com,telegraph.co.uk,bbc.com,reddit.com&language=en&sortBy=publishedAt&apiKey=" + api_key
    news = requests.get(url).json()

    articles = news["articles"]

    my_articles = []
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])

    for i in range(10):
        my_news =my_news + my_articles[i] + "\n"

    label.config(text = my_news)

canvas = tk.Tk()
canvas.geometry("900x600")
canvas.title("GUI News Feed")
label = tk.Label()

label = tk.Label(canvas, font=18, justify="left")
label.pack(pady=20)

getNews()

canvas.mainloop()

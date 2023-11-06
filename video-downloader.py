from tkinter import *
from pytube import YouTube
from time import sleep

window = Tk()
window.title("Vídeo Downloader")

window.geometry("500x500")
window.configure(background="gray", pady=-20, padx=30)

url_label = Label(window, text="Insira a url do vídeo no campo abaixo", font="Verdana")
url_label.configure(background="gray")
url_label.grid(padx=30, column=0, row=0)

url_input = Entry(window,width=45, background="white", border=0.5)
url_input.grid(column=0, row=1)
url_input.configure(borderwidth=0)
url_input.focus()

download_label = Label(window, text=" ")

def downloadVideo():
    download_label.grid(column=0, row=3)
    link = url_input.get()
    yt = YouTube(link)
    video = yt.streams.get_highest_resolution()
    video.download()
    download_label.configure(text="Baixado com sucesso!", background="gray")
    

button = Button(window,command=downloadVideo, width=25, justify="center", border=0.5, text="Baixar")
button.grid(column=0, row=2, pady=5)



window.mainloop()
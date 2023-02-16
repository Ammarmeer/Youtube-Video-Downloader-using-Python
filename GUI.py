from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x400')
root.resizable(0, 0)
root.title("Youtube Video Downloader")

Label(root, text='Youtube Video Downloader', font='arial 20 bold').pack()

link = StringVar()
quality = StringVar()

Label(root, text='Paste Link Here:', font='arial 15 bold').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)

Label(root, text='Select Quality:', font='arial 15 bold').place(x=180, y=120)

quality_choices = ['1080','720p', '480p', '360p', '240p', '144p']
quality.set(quality_choices[0])

quality_dropdown = OptionMenu(root, quality, *quality_choices)
quality_dropdown.config(width=20, font='arial 12')
quality_dropdown.place(x=170, y=150)

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.filter(res=quality.get()).first()
    if video is not None:
        video.download()
        Label(root, text='Video Downloaded', font='arial 15').place(x=180, y=270)
    else:
        Label(root, text='Error: Video not available in selected quality', font='arial 15').place(x=50, y=270)


Button(root, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red', padx=2, command=Downloader).place(x=180, y=210)

root.mainloop()

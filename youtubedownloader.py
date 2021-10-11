from tkinter import *
import tkinter.font as font
from pytube import YouTube
from tkinter import messagebox
import os

def download():
    url=url_entry.get()
    yt = YouTube(url)
    parent_dir = os.path.expanduser('~/Downloads')
    
    if music_checkbox.get()==1 or video_checkbox.get()==1:
        if music_checkbox.get()==1 and video_checkbox.get()==1:
            audio = yt.streams.filter(only_audio=True).first()
            dwnld_file = audio.download(parent_dir)
            base = os.path.splitext(dwnld_file)[0]
            os.rename(dwnld_file, base + ".mp3")
            video = yt.streams.get_highest_resolution().download(parent_dir)
            Label(height="2").pack()
            messagebox.showinfo(title="Download Successfull", message="Check your Downloads folder")
            
        elif music_checkbox.get()==1:
            audio = yt.streams.filter(only_audio=True).first()
            dwnld_file = audio.download(parent_dir)
            base = os.path.splitext(dwnld_file)[0]
            os.rename(dwnld_file, base + ".mp3")
            Label(height="2").pack()
            messagebox.showinfo(title="Mp3 Download Successfull", message="Check your Downloads folder")
            
        else:
            video = yt.streams.get_highest_resolution().download(parent_dir)
            Label(height="2").pack()
            messagebox.showinfo(title="Video Download Successfull", message="Check your Downloads folder")
    
    else:
        Label(height="10").pack()
        messagebox.showinfo(title="Warning", message="Please select either M3 or Video")

window = Tk()
window.title("Youtube Downloader")
url_entry=StringVar()

fontstyle = font.Font(family='Helvetica', size="20")
heading_label=Label(text="Welcome to Youtube Downloader",font=fontstyle,background="black", foreground="White",width="200",height="4").pack()
url_label=Label(text="Enter URL ").pack()
Entry(width="50",textvariable=url_entry).pack()

music_checkbox = IntVar()
video_checkbox = IntVar()

Checkbutton(window, text = "MP3", variable = music_checkbox, onvalue = 1, offvalue = 0).pack()
Checkbutton(window, text = "Video", variable = video_checkbox, onvalue = 1, offvalue = 0,).pack()


download_button = Button(text="Download",background="black",foreground="white", command = download).pack()
window.mainloop()
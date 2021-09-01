# Import module
from __future__ import unicode_literals
import tkinter as tk
from tkinter import filedialog,messagebox
from tkinter import Text
from pydub import AudioSegment
import youtube_dl
import glob,os
from threading import *

# Create object
root = tk.Tk()
root.title("Youtube Downloader")
root.config(bg="grey")
# Adjust size
root.geometry("700x500")
root.resizable(width=0,height=0)

# Add text
label2 = tk.Label(root, text = "Welcome to Youtube Downloader")

label2.pack(pady = 50)

# Create Frame
frame1 = tk.Frame(master=root,width=700,height=500,bg="grey")
frame1.pack()

def folderChooser():
    folder_destination = filedialog.askdirectory(title="select file")
    print(folder_destination)
    os.chdir(folder_destination)

def threading():
    t1=Thread(target=download)
    t1.start()

def download():
    inp = inputUrl.get("1.0","end-1c")
    urls = inp.split(",")
    txtfiles = []
    ydl_opts = {"format":"mp4"}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls)

    for file in glob.glob(os.getcwd()+"/*.mp4"): 
            txtfiles.append(file)
    
    for i in range(len(txtfiles)):
            src = txtfiles[i]
            dst = txtfiles[i].replace(".mp4","") + ".mp3"
            sound = AudioSegment.from_file(src)
            sound.export(dst,format="mp3")
            os.remove(txtfiles[i])

    messagebox.showinfo("Completed","Download has been completed.")

# Add buttons

button1 = tk.Button(frame1, text = "Choose Destination Folder: ",command=folderChooser)
button1.pack(pady=30)

inputUrl = Text(master=root,height=10,width=42,bg="white")
inputUrl.pack(pady=5)

button3 = tk.Button(frame1, text = "Download: ",command=threading)
button3.pack(pady=40)

# Execute tkinter
root.mainloop()

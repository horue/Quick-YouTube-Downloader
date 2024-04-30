import customtkinter as ct
from pytube import YouTube
import os
from CTkMessagebox import CTkMessagebox




def show_options(e1, l2, root):
    try:
        yt = YouTube(e1.get())
    except:
        CTkMessagebox(title='Info', message='Missing Link.', icon='question')
    title = yt.title
    l2.configure(text=title)
    for i in range(7):
        bi=ct.CTkButton(root, text=f'Download - Opção {i+1}')
        bi.pack(pady=10)

def main(root):
    l1=ct.CTkLabel(root, text='Quick YouTube Downloader')
    l1.pack(pady=20)

    e1=ct.CTkEntry(root, placeholder_text="Enter the link")
    e1.pack(pady=20)

    b1=ct.CTkButton(root, text="Show download options", command=lambda:show_options(e1, l2, root))
    b1.pack()

    l2=ct.CTkLabel(root, text='No video yet.')
    l2.pack(pady=20)

def root():
    root = ct.CTk()
    root.geometry("500x650")
    root.title("Quick YouTube Downloader")

    
    main(root)
    
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

root()
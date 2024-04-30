import customtkinter as ct
from pytube import YouTube
import os



def show_options(e1):
    print(1)


def main(root):
    l1=ct.CTkLabel(root, text='Quick YouTube Downloader')
    l1.pack(pady=20)

    e1=ct.CTkEntry(root, placeholder_text="Enter the link")
    e1.pack(pady=20)

    b1=ct.CTkButton(root, text="Show download options", command=lambda:show_options(e1))
    b1.pack()

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
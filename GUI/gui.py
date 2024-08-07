import customtkinter as ct
from pytube import YouTube
from CustomTkinterMessagebox import *
from tkinter import *


################ IMPORTATNT! ######################
## If you are running the code, you MUST change  ##
## cipher.py file from pytube. At line 30, the   ##
## regex MUST be changed to                      ##
## var_regex = re.compile(r"^(\w|\$)+\W")        ##
## otherwise it wont work.                       ##
###################################################



def download(s, a):
    if s:
        final_video = s
        final_video.download(output_path = 'Desktop')
    if a:
        final_audio = a
        final_audio.download(output_path = 'Desktop')



def show_options(e1, l2, f1):
    try:
        yt = YouTube(e1.get())
        for widget in f1.winfo_children():
            widget.destroy()
    except:
        CTkMessagebox.messagebox(title='Warning!', text='Error. No link was given.')
    e1.delete(0, 'end')
    title = yt.title
    streams = yt.streams.filter(progressive=True)
    audios = yt.streams.filter(only_audio=True)
    l2.configure(text=title)
    for i, stream in enumerate(streams):
        bi=ct.CTkButton(f1, text=f'Download - Option {stream}', command=lambda s=stream:download(s, None))
        bi.pack(pady=10)
    for i, audio in enumerate(audios):
        bi2=ct.CTkButton(f1, text=f'Download - Option {audio}', command=lambda a=audio:download(None, a))
        bi2.pack(pady=10)



def main(root):
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Arquivo", menu=filemenu)

    l1=ct.CTkLabel(root, text='Quick YouTube Downloader')
    l1.pack(pady=20)

    e1=ct.CTkEntry(root, placeholder_text="Enter the link")
    e1.pack(pady=20)

    b1=ct.CTkButton(root, text="Show download options", command=lambda:show_options(e1, l2, f1))
    b1.pack()

    l2=ct.CTkLabel(root, text='No video yet.')
    l2.pack(pady=20)

    f1 = ct.CTkFrame(root, height=1000, fg_color='transparent')
    f1.pack(fill="x")



def root():
    root = ct.CTk()
    root.geometry("500x650")
    root.title("Quick YouTube Downloader")
    root.iconbitmap(r'Visual Stuff\icon.ico')
    
    main(root)
    
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

root()
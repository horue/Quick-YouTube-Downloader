import customtkinter as ct
from pytube import YouTube
from CTkMessagebox import CTkMessagebox


def download(s, a):
    if s:
        final_video = s
        final_video.download(output_path = 'Desktop')
    if a:
        final_audio = a
        final_audio.download(output_path = 'Desktop')



def show_options(e1, l2, root):
    try:
        yt = YouTube(e1.get())
    except:
        CTkMessagebox(title='Info', message='Missing Link.', icon='question')
    title = yt.title
    streams = yt.streams.filter(progressive=True)
    audios = yt.streams.filter(only_audio=True)
    l2.configure(text=title)
    for i, stream in enumerate(streams):
        bi=ct.CTkButton(root, text=f'Download - Option {stream}', command=lambda s=stream:download(s, None))
        bi.pack(pady=10)
    for i, audio in enumerate(audios):
        bi2=ct.CTkButton(root, text=f'Download - Option {audio}', command=lambda a=audio:download(None, a))
        bi2.pack(pady=10)

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
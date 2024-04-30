import customtkinter as ct

def main(root):
    l1=ct.CTkLabel(root, text='Quick YouTube Downloader')
    l1.pack(pady=20)

    e1=ct.CTkEntry(root, placeholder_text="Enter the link")
    e1.pack(pady=20)

def root():
    root = ct.CTk()
    root.geometry("500x350")
    root.title("Quick YouTube Downloader")

    
    main(root)
    
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

root()
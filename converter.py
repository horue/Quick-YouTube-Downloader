from pytube import YouTube



def download(video):
    yt = YouTube(video)
    title=yt.title
    a=input(f'Download {title}? (Y/N) ')
    if a == 'Y' or a == 'y':
        print('Downloading...')
        yt.download()
    else:
        return



video=input('Enter the link to the video: ')
download(video)
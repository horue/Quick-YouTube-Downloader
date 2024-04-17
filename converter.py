from pytube import YouTube



def download(video):
    yt = YouTube(video)
    title=yt.title
    a=input(f'Download {title}? (Y/N) ')
    if a == 'Y' or a == 'y':
        print('Downloading...')
        yt.streams.filter(progressive=False, file_extension='mp4').order_by('resolution').last().download()
    else:
        return



video=input('Enter the link to the video: ')
download(video)
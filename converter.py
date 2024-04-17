from pytube import YouTube



def download(video):
    yt = YouTube(video).streams.last().download()
    title=yt.title
    yt.streams
    filter(progressive=True, file_extension='mp4')
    yt.order_by('resolution')
    yt.desc()
    yt.last()
    a=input(f'Download {title}? (Y/N) ')
    if a == 'Y' or a == 'y':
        print('Downloading...')
        yt.download()
    else:
        return



video=input('Enter the link to the video: ')
download(video)
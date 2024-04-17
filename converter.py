from pytube import YouTube



def download(video):
    yt = YouTube(video)
    title=yt.title
    streams = yt.streams.filter(progressive=True)


    print('Download options: ')
    for i, stream in enumerate(streams):
        print(f'{i+1} - {stream}')

    a=input(f'Download {title}? (Y/N) ')
    if a == 'Y' or a == 'y':
        print('Downloading...')
        yt.download()
        main()
    else:
        return


def main():
    video=input('Enter the link to the video: ')
    download(video)
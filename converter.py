from pytube import YouTube



def download(video):
    yt = YouTube(video)
    title=yt.title
    streams = yt.streams.filter(progressive=True)
    audios = yt.streams.filter(only_audio=True)


    print('Download options: ')
    for i, stream in enumerate(streams):
        print(f'{i+1} - {stream}')
    for i, audio in enumerate(audios):
        print(f'{i+len(streams)+1} - {audio}')


    a=input(f'What option do you want to download {title}? ')
    if a == 'Y' or a == 'y':
        print('Downloading...')
        yt.download()
        main()
    else:
        return


def main():
    video=input('Enter the link to the video: ')
    download(video)
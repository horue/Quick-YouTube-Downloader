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


    a=int(input(f'What option do you want to download {title}? '))
    a2=a - 1 
    if a2 < len(streams):
        selected_stream = streams[a2]
    else:
        selected_stream = audios[a2 - len(streams)]
    print('Downloading...')
    selected_stream.download()
    print('Download complete!')
    main()



def main():
    video=input('Enter the link to the video: ')
    download(video)
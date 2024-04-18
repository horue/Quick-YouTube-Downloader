from pytube import YouTube
import os

def download(video, output):
    try:
        yt = YouTube(video)
    except Exception as e:
        print(f'An error occurred: {e}')
    title=yt.title
    streams = yt.streams.filter(progressive=True)
    audios = yt.streams.filter(only_audio=True)


    print('Download options: ')
    print('')
    print( '-' *5 + '< Video Options >' +'-' *5)
    print('')
    for i, stream in enumerate(streams):
        print(f'{i+1} - {stream}')
    print('')
    print( '-' *5 + '< Audio Options >' +'-' *5)
    print('')
    for i, audio in enumerate(audios):
        print(f'{i+len(streams)+1} - {audio}')

    print('')
    a=int(input(f'What option do you want to download {title}? '))
    a2=a - 1 
    if a2 < len(streams):
        selected_stream = streams[a2]
    else:
        selected_stream = audios[a2 - len(streams)]
    print('Downloading...')
    selected_stream.download(output_path=output)
    print('Download complete!')
    main()



def main():
    output = os.path.join(os.path.expanduser("~"), "Documents\\Quick YouTube Downloader")
    video=input('Enter the link to the video: ')
    print('')
    download(video, output)
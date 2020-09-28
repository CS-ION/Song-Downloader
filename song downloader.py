import shutil
import youtube_dl
from youtubesearchpython import SearchVideos
import os

def search(song_name):

    result = SearchVideos(song_name,offset=1,mode='dict',max_results=1)
    results = result.result()
    for I in results['search_result']:
        print('Is this you want to download (Y/N)')
        print(I['title'])
        x = input()
        if x.lower()=='n':
            return
        download(I['link'])
        print(f"{I['title']} was succesfully downloaded")

def download(url):

    ytdl_format_options = {
                'format' : 'bestaudio/best' ,
                'postprocessors' : [{
                       'key' : 'FFmpegExtractAudio' ,
                       'preferredcodec' : 'mp3' ,
                       'preferredquality' : '192' ,
                       }]
                }

    ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
    ytdl.download([url])

    move()
    
def move():
    for file in os.listdir():
        if file.endswith('mp3'):
            shutil.move(file,r'E:')

choice = 'Y'
while choice == 'Y':
    print('enter the song')
    song = input()   
    search(song)
    print('Do you want to download more songs? (Y/N')
    choice = input()

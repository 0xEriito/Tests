from pytube import YouTube
import os

link = input("enter a link: ")
yt = YouTube(link)
streams = yt.streams.filter(progressive=True, file_extension='mp4')
dpath = os.path.expanduser("~/Desktop/videos")




print(f"title: {yt.title}\nviews: {yt.views}")

down = input("do you want to download? (y/n)  ")
if down == "y" :
    print("choose a resolution from the list: ")
    
    for stream in streams :
        print(f"resolution: {stream.resolution}\nfile size: {stream.filesize_mb:.2f}mb\n")
    
    chosenRes = input("resolution: ")
    if chosenRes == "144p" or "240p" or "360p" or "480p" or "720p" or "1080p" :
        print("downloading...")
        stream = yt.streams.filter(progressive=True, file_extension='mp4', res= chosenRes).first()
        stream.download(output_path=dpath)
        print(f"video has been downloaded to : {dpath}")
    else :
        print("wrong input, try again")
elif down == "n" :
    print("have a good one")
else :
    print("wrong choice")

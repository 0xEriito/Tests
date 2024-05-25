from pytube import YouTube
import os

print(f"*****WELCOME TO YOUTUBE DOWNLOADER*****\n")


link = input("Enter a Link Please: ")
yt = YouTube(link)
dpath = os.path.expanduser("~/Desktop/videos")
ress = ['144p' , '240p' , '360p', '480p' , '720p' , '1080p']


def basic(yt):
    
    print(f"Title: {yt.title}\nViews: {yt.views}")


def download(yt):
    
    print("Choose a Resolution From The Provided:")
    
    streams = yt.streams.filter(progressive=True, file_extension='mp4')
    
    for stream in streams :
        print(f"Resolution: {stream.resolution}\nFile Size: {stream.filesize_mb:.2f}MB\n")
        
    chose = input()
    
    if chose in ress :
        print("Downloading...")
        stream = yt.streams.filter(progressive=True, file_extension='mp4', res= chose).first()
        stream.download(output_path=dpath)
        print(f"The Video Has Been Downloaded to : {dpath}")


def main():

    basic(yt)

    dld = input("Do You Want To Download This Video? (y/n)  ")

    if dld == "y":
        download(yt)
    elif dld == "n":
        print("Have a Good Day!")
    else:
        print("Unavailable Choice, Please Try Again!")


if __name__ == "__main__":
    main()
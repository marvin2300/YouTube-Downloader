from pytube import YouTube
import var

#var.url = "https://www.youtube.com/watch?v=zI383uEwA6Q"
#var.res = "1080p"

def dl_video():
    print("Downloading video...")
    print(var.url)
    print(var.res)
    YouTube(var.url).streams.filter(res=var.res, progressive=False).first().download(filename="temp_video.webm",
                                                                                     output_path="./temp_files")
    print(f"Finished downloading '{var.title}'")


def dl_audio():
    print("Downloading audio...")
    YouTube(var.url).streams.filter(abr="160kbps", progressive=False).first().download(filename="temp_audio.webm",
                                                                                   output_path="v4/temp_files")
    print(f"Finished downloading '{var.title}'")

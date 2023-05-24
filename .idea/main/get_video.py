from pytube import YouTube
import var
# url = "https://www.youtube.com/watch?v=zI383uEwA6Q"


def get_data():
    print("Which resolution would you like to download?")
    acc_res = []
    for i in YouTube(var.url).streams.filter(mime_type='video/webm', progressive=False):
        acc_res.append(i.resolution)
    print(acc_res)

    while True:
        var.res = input("Enter the resolution you want to download: ")
        if var.res in acc_res:
            print("Downloading video...")
            break
        else:
            print("Not a valid resolution. Please try again.")

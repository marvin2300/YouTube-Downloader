import re
from pytube import YouTube
import var

# https://www.youtube.com/watch?v=zI383uEwA6Q


def is_youtube_link(url):
    youtube_regex = \
        r"(?:https?://)?(?:www\.)?youtu(?:\.be/|be\.com/(?:watch\?v=|v/|embed/|user/|playlist\?list=))(?:[^\s&?]+)"
    return re.match(youtube_regex, url) is not None


def youtube_link_validation():
    while True:
        var.url = input("Please enter your YouTube URL: ")
        if is_youtube_link(var.url):
            while True:
                yt = YouTube(var.url)
                var.title = yt.title
                choice = input("You want to download: '" + yt.title + "'\nIs that correct? (y/n): ")
                if choice.lower() == "n":
                    break
                elif choice.lower() == "y":
                    return var.url
                else:
                    print("Invalid input. Please try again.")
        else:
            print("Invalid URL, please try again.")
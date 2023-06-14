import ffmpeg
import os
# os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"


def merge():
    filename = input("How do you want to name your file?: ")
    print("Start merging AV Files...")
    video = ffmpeg.input('./temp_files/temp_video.mp4')
    audio = ffmpeg.input('./temp_files/temp_audio.mp3')

    ffmpeg.output(audio, video, "./final_videos/" + filename + ".mp4").run(overwrite_output=True)

    print("Cleaning up...")
    os.remove("./temp_files/temp_audio.mp3")
    os.remove("./temp_files/temp_video.mp4")
    os.remove("./temp_files/temp_audio.webm")
    os.remove("./temp_files/temp_video.webm")
    print("Done!")


# merge()

import moviepy.editor as moviepy


def convert_video():
    print("Converting Video...")
    con_video = moviepy.VideoFileClip("./temp_files/temp_video.webm")
    con_video.write_videofile('./temp_files/temp_video.mp4')


def convert_audio():
    print("Converting Audio...")
    con_audio = moviepy.AudioFileClip("./temp_files/temp_audio.webm")
    con_audio.write_audiofile('./temp_files/temp_audio.mp3')

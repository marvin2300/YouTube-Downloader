import yt_input
import get_video
import hd_file_download
import file_convert

# https://www.youtube.com/watch?v=zI383uEwA6Q

# global url
# global res

yt_input.youtube_link_validation()
get_video.get_data()
hd_file_download.dl_video()
hd_file_download.dl_audio()
file_convert.convert_video()
file_convert.convert_audio()
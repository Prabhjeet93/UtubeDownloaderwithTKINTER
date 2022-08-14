from pytube import YouTube

link = "https://www.youtube.com/watch?v=Dx_c6GTw"
yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)
reslution='720p'
#yd = yt.streams.get_highest_resolution()
yd = yt.streams.get_audio_only()
#yd =yt.streams.get_by_resolution(reslution)
# ADD FOLDER HERE
yd.download('YTDownloader')

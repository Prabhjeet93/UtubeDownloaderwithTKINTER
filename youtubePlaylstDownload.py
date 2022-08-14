from pytube import YouTube, Playlist

# this code will download all the videos/audios in the provided playlist. only change line no. 12 for the videos.

link = "https://www.youtube.com/playlist?list=kf7bMh3LXlAH0X"
ytp = Playlist(link)
print(link)
print(len(ytp.videos))
for video in ytp.videos:
    print("Title: ", ytp.title)
    #print("View: ", ytp.views)
    ytp=video.streams.get_audio_only()
    # ADD FOLDER HERE
    ytp.download('songs1')

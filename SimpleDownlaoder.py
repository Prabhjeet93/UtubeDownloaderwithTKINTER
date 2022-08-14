import tkinter as tk
from tkinter import ttk

from tkinter import messagebox, END
# Utilize tkinter class to accomplish the following:
#
# Create a window with an appropriate title
from tkinter.messagebox import showinfo

from pytube import YouTube

# Method created for the download button, which will take url and location and download the audio song
def downloadVideo(): 
    urltxt = urlfield.get()
    locationText=locationfield.get()

    #link = "https://www.youtube.com/watch?v=yV-Rb-zqong"
    yt = YouTube(urltxt)
    print("Title: ", yt.title)
    print("View: ", yt.views)
    # yd = yt.streams.get_highest_resolution()
    yd = yt.streams.get_audio_only()

    # ADD FOLDER HERE
   # yd.download('/Users/HP/Downloads/YTDownloader')
    yd.download(locationText)
    messagebox.showinfo("message","Downloading the Requested video")



window = tk.Tk()
window.geometry("800x600")    ## size of the window defined
window.title('YouTube Downloader')  ## Title of the window defined
window_title = tk.Label(text = "Welcome to the Youtube Downloader",    ## main heading of the page defined
                        foreground="blue",   ## color of the text defined
                        background="Red",   ## background color of the label box is defined
                        width = 80,    ### width of the label box is defined
                        height=2)    ### Height of the label box is defined

window_title.grid(row=1, column=2)
#window_title.pack()
url = tk.Label(window, text="Enter YouTube URL", bg="red")   # Create a Day label
url.grid(row=3, column=0)          #set the Position of the Enter url text on the main screen
urlfield = tk.StringVar()           # Define Day field variable as String
urlfield = tk.Entry(window)             # Create a text entry box for the url
urlfield.grid(row=3, column=1)          #set the Position of the Enter urlfield box on the main screen

location = tk.Label(window, text="Enter Location for download", bg="red")   # Create a Day label
location.grid(row=5, column=0)          #set the Position of the Enter location text on the main screen
locationfield = tk.StringVar()           # Define location field variable as String
locationfield = tk.Entry(window)             # Create a text entry box for the location
locationfield.grid(row=5, column=1)          #set the Position of the Enter locationfield box on the main screen



btn_download = tk.Button(window, text="Download", fg="Red", bg="Black", command=downloadVideo)
btn_download.grid(row=4, column=2)
window.mainloop()       # Start the GUI with above mention methods and labels




# From the  installed Pytube module, import the youtube library
from pytube import YouTube 

link = "https://www.youtube.com/watch?v=EDZ25anwgjc"
yt = YouTube(link)

#Title of video
print("Title: ",yt.title)
#Number of views of video
print("Number of views: ",yt.views)
#Length of the video
print("Length of video: ",yt.length,"seconds")
#Rating
print("Ratings: ",yt.rating)
#printing all the available streams
# yt.streams

#Getting the highest resolution possible
ys = yt.streams.filter(progressive=True).get_highest_resolution()

#Starting download
print("Downloading...")
ys.download()
print("Download completed!!")
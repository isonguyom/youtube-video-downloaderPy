# Youtube Video Downloader
from pytube import YouTube



print("WELCOME! THIS IS A YOUTUBE VIDEO DOWNLOADER")

try:
    # Request of number of youtube videos to be downloader
    num_of_videos = int(input("How many videos do you want to download? "))

    links = []
    for i in range(num_of_videos):
        video_link =  input("Enter youtube video link: ")

        links.append(video_link)

    print(links)

    for i in links:
        print("\n---------------------------------------------------------------------")
        yt = YouTube(i)
        #Title of video
        print("Title: ",yt.title)
        #Number of views of video
        print("Number of views: ",yt.views)
        #Length of the video
        print("Length of video: ",yt.length,"seconds")
        #Rating
        print("Ratings: ",yt.rating)
        print("---------------------------------------------------------------------")

except:
    print("You didn't input a legal integer.")
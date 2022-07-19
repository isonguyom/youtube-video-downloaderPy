# Youtube Video Downloader
from pytube import YouTube



print("\nWELCOME! THIS IS A YOUTUBE VIDEO DOWNLOADER")

try:
    # Request of number of youtube videos to be downloader
    num_of_videos = int(input("How many videos do you want to download? "))

    links = []
    for i in range(num_of_videos):
        video_link =  input("Enter youtube video link: ")

        links.append(video_link)

    print(links)
    print("\n---------------------------------------------------------------------")
    for i in links:
        print("Video", links.index(i)+1)
        yt = YouTube(i)

        # Video Description  
        print("Title: ",yt.title) #Title of video       
        print("Length of video: ",yt.length,"seconds") #Length of the video        
        print("Ratings: ",yt.rating) #Rating
        
        print("Downloading...", links.index(i)+1, "/", len(links))
        
        
        print(links.index(i)+1, "of", len(links), "downloaded")
        print("---------------------------------------------------------------------\n")

except:
    print("You didn't input a legal integer.")
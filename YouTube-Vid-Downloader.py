from pytube import YouTube

link = input("Please Enter The Video's URL: ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()
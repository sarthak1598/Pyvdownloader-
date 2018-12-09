# the script code
import pytube 

yobject = YouTube(str(input("Enter the video link: "))) #initialised the object 
videos = yobject.get_videos()

m = 1
for v in videos:
    print(str(m)+". "+str(v))
    m = m+1

n = int(input("Enter the number of the video: "))
videoo = videos[n-1]

destination = str(input("Enter the destination: ")) # the path where you want to keep the downloaded file 
videoo.download(destination)  

print(yobject.filename+"\nHas been successfully downloaded")

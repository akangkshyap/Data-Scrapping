#Author: Akangkshya Pathak
import csv
from pytube import YouTube
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



with open('data.csv', 'r') as file:
   reader = csv.reader(file)
   for row in reader:
      url = row[0]
      my_video = YouTube(url)
      GET https://www.googleapis.com/youtube/v3/activitiespart=snippet%2CcontentDetails&channelId={row[0]}&maxResults=25&regionCode=tw&key={#Enter the google API key}
      print("Video Title")
      print(my_video.title)
      print("Download video") 
      my_video = my_video.streams.get_highest_resolution()
      print(row[0])
      my_video.download('E:/7th sem CSE/internship/Video')#Location where the videos are to be saved.

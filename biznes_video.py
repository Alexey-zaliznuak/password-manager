from pytube import YouTube
from os import system


urls = [
    "https://www.youtube.com/watch?v=GxVxFJTxQPY&feature=youtu.be",
    "https://www.youtube.com/watch?v=vX33YC1luK0&feature=emb_logo",
    "https://www.youtube.com/watch?v=723d3pqEn90&feature=youtu.be",
    "https://www.youtube.com/watch?v=Ylzqbxfgiqo&feature=youtu.be",
    "https://www.youtube.com/watch?v=hH7mCL8Zmqo&feature=youtu.be",
    "https://www.youtube.com/watch?v=Fsp94GrrcMY&feature=youtu.be",
    "https://www.youtube.com/watch?v=sKHDG2jbCyo&feature=youtu.be",
    "https://www.youtube.com/watch?v=h3Cj9yRfQQM&feature=youtu.be",
    "https://www.youtube.com/watch?v=LJdnN64JIm4&feature=youtu.be",
]

for i in range(9):
    print(f"Скачивание видео ({i+1})")
    YouTube(str(urls[i])).streams.first().download("C:\\biznes_videos")
    
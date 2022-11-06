from youtubesearchpython import VideosSearch
from pytube import YouTube  

def get_youtube_video(query, path, limit=3):
    videosSearch = VideosSearch(query)
    result = videosSearch.result()['result']
    filtered_result = []
    for x in result:
        minutes, seconds = (["0", "0"] + x["duration"].split(":"))[-2:]
        if int(minutes) <= 5:
            filtered_result.append(x)
            limit -= 1
            if limit == 0:
                break

    i = 1
    for v in filtered_result:
        yt = YouTube(v["link"])
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(path)
        i += 1   
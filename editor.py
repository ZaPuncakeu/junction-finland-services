from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx
from youtube import get_youtube_video
import os

def edit_youtube_video(idv, query, clip_num=3):
    get_youtube_video(query, f"../server/videos/public/{idv}/", clip_num)
    arr = os.listdir(f'../server/public/{idv}')
    clips = [VideoFileClip(f"../server/videos/public/{idv}/{v}").subclip(10, 20) for v in arr]
    combined = concatenate_videoclips(clips)
    combined.write_videofile(f"../server/public/videos/{idv}/{idv}.mp4")
    video = f'http://127.0.0.1:4001/videos/{idv}/{idv}.mp4'
    
    return video

def edit_videos(idv, files):
    os.mkdir(f'../server/public/videos/{idv}')
    clips = [VideoFileClip(file).subclip(10, 20) for file in files]
    combined = concatenate_videoclips(clips)
    combined.write_videofile(f"../server/public/videos/{idv}/{idv}.mp4")
    
    for i in range(len(files)):
        clips[i].close()
        if os.path.exists(files[i]):
            os.remove(files[i])
        else:
            print("The file does not exist")

    video = f'http://127.0.0.1:4001/videos/{idv}/{idv}.mp4'
    return video
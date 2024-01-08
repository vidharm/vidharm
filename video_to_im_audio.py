import subprocess
from os.path import join
import os
import json
import glob

path = "clips"
new_path = "im_audio"
filenames = [a["filename"] for a in json.load(open("refined_annotations.json","r")).values()]
for filename in filenames[:5]:
    path_to_video = join(path,filename,f"{filename}.mp4")
    try:
        os.makedirs(join(new_path,filename))
    except:
        if len(os.listdir(join(new_path,filename))) > 0:
            continue
    subprocess.call(["ffmpeg","-y","-i",path_to_video,f"{join(new_path,filename,filename)}.wav"])
    subprocess.call(["ffmpeg","-y","-i",path_to_video,"-q:v", "1",f"{join(new_path,filename,filename)}_%d.jpg"])
import librosa
import subprocess
from os.path import join
import os
import json
import glob
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
#mu = -28.393
#std = 17.323

path = "im_audio"
filenames = [a["filename"] for a in json.load(open("annotations.json","r")).values()]
N = len(filenames)
for filename in tqdm(filenames):
    if os.path.exists(join(path,filename,f"{filename}.npy")):
        continue
    path_to_wav = join(path,filename,f"{filename}.wav")
    y, sr = librosa.load(path_to_wav,sr=None)
    n_fft = int(round(sr * 32 / 1000)) #Transform with 32 ms fourier transform
    hop_length = n_fft//2
    fmin = 20
    fmax = 15000
    M = librosa.feature.melspectrogram(y, sr, n_fft=n_fft, hop_length=hop_length, window='hann', center=True, pad_mode='reflect', power=2.0,fmin=fmin,fmax=fmax)
    M = librosa.power_to_db(M)
    np.save(join(path,filename,f"{filename}.npy"),M)
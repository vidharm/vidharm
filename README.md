# VidHarm: A dataset for detection of harmful content in video

## Info

Splits for the dataset are available in this repo. They are lists with dictionary entries saved in json format.
Each entry has the following keys:

* filename: The unique id of the clip
* label: A single or list of labels from the label set ("BT,"7","11","15")
* total_frames: The total number of frames in the clip (this number is adapted to the preprocessed dataset, see info below)
  
## Download links

## Raw Clips
The raw clips are available at <a href="https://liuonline-my.sharepoint.com/:u:/g/personal/johed13_liu_se/EbW2j_Dm5btBqa3XRucfuXYBebj4upFJAiPeJsQqkUcAvg?e=RyNv1r">this url.</a>.
The password is "vidharm". 
The clips are encoded in mostly h264. The folder structure is:

```bash
├── clips
│   ├── ID_FIRST
│   │   ├── ID_FIRST.mp4
│   ...
│   ├── ID_LAST
│   │   ├── ID_LAST.mp4
```

## Preprocessed Images and Audio
Since online video learning can be very CPU intensive we will also provide a preprocessed dataset containing each clip split into individual frames (jpeg encoded) + an additional log mel spectrogram for the audio.
For access to these, please send an email to <a href="mailto:johan.edstedt@liu.se">johan.edstedt@liu.se</a>

```bash
├── preprocced_clips
│   ├── ID_FIRST
│   │   ├── ID_FIRST_1.jpg
|   |   ...
│   │   ├── ID_FIRST_N.jpg
│   │   ├── ID_FIRST.npy
│   │   ├── ID_FIRST.wav
│   ...
│   ├── ID_LAST
│   │   ├── ID_LAST_1.jpg
|   |   ...
│   │   ├── ID_LAST_N.jpg
│   │   ├── ID_LAST.npy
│   │   ├── ID_LAST.wav
```

## Reproducing Results

Go to https://github.com/Parskatt/is-this-harmful, for code and evaluation.

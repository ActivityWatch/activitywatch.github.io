#!/bin/bash
video_source=gource.mp4
audio_source="C418 - Alpha (Minecraft Volume Beta)-xLfm2nnCOpc.mp3"
audio_offset="00:03:08.0"
audio_end="09:00:00"

ffmpeg -ss "$audio_offset" -to "$audio_end" \
        -i "$audio_source" \
        -i "$video_source" \
       -vcodec copy -acodec libmp3lame \
       output.mp4

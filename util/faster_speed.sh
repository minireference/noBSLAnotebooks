#!/bin/bash

# via https://trac.ffmpeg.org/wiki/How%20to%20speed%20up%20/%20slow%20down%20a%20video
echo "Converting $1 to 1.5x speed..."
ffmpeg -i "$1"  -filter_complex "[0:v]setpts=0.6666666666666*PTS[v];[0:a]atempo=1.5[a]" -map "[v]" -map "[a]" "tmp-$1"

# via http://alien.slackbook.org/blog/fixing-audio-sync-with-ffmpeg/
echo "Delaying audio of $1 by 60ms"
ffmpeg -i "tmp-$1" -itsoffset 0.06 -i "tmp-$1" -map "0:0" -map "1:1" -acodec copy -vcodec copy  "faster-$1"

# cleanup temp file
rm "tmp-$1"


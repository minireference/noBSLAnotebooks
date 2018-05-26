#!/usr/bin/env bash
set -e

OUTDIR='aspynb'

for ipynbfile in `ls *.ipynb`; do
  nbname=$(basename "$ipynbfile" ".ipynb")
  echo "Processing $nbname.ipynb --> $OUTDIR/$nbname.py"
  pynb --import-ipynb "$ipynbfile" \
       --no-exec \
       --disable-footer \
       --log-level ERROR \
       --export-pynb $OUTDIR/"$nbname".py
  git add aspynb
done

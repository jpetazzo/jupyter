#!/bin/sh
rsync -av \
  --exclude work/.ipynb_checkpoints/ \
  --exclude .git \
  ./ jupyter@185.145.250.49:jupyter/

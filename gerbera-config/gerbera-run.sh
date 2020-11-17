#!/bin/bash
# Start a docker container for pigallery2
docker run -d \
   --name gerbera \
   -p 49152:49152 \
   -p 1900:1900 \
   -v gerbera_root:/root \
   -v /data/media:/data \
   gerbera/gerbera:latest

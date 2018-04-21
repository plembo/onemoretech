#!/bin/bash
# Cleanup backup files
HOME=/root
BUDIR=/data/backup

echo "Cleanup backup files in $BUDIR"
echo `date`
echo "media"
find ${BUDIR}/media -name "*.gz" -type f -mtime +10 -exec rm -f {} \;
echo "homes"
find ${BUDIR/homes -name "*.gz" -type f -mtime +10 -exec rm -f {} \;


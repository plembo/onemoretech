#!/bin/bash
# Converts Evernote HTML export to markdown text.

export_dir=$HOME/projects/export
clean_dir=$HOME/projects/clean
import_dir=$HOME/projects/import

cd $export_dir
for f in * 
do
  strings "$f" > "$clean_dir/$f"
done

cd $clean_dir
for f in *
do
  python-html2text "$f" > "$import_dir/$f.md"
done


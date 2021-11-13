#!/bin/bash
set -e

echo "START Running Writer on `date`"
#python3 -u logoutput_writer.py >> index.html &
python3 -u logoutput_writer.py >> files/file.txt
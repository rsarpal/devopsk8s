#!/bin/bash
set -e

echo "START Running Django on `date`"
python3 logoutput.py #>> index.html &
#python3 -m http.server 8000
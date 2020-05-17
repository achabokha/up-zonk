#!/bin/zsh

echo "Starting nodemon for templates debuging..."
echo "It will monitor *.py and *.mustache files and restart python3"

nodemon --exec "python3 ./src/genie.py product" --ext py,mustache,yaml

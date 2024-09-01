#!/bin/zsh

echo "Starting nodemon for templates debuging..."
echo "It will monitor py, mustache, yaml and json files and restart python3"

nodemon --exec "python3 ./src/genie.py product" --ext py,mustache,yaml,json

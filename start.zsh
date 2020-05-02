#!/bin/zsh

echo "Starting nodemon for templates debuging..."
echo "It will monitor *.py and *.mustache files and restart python3"

nodemon --exec "python3 " ./src/genie.py ./models/product.json ./templates/entity.mustache ./out/entities --ext py,mustache

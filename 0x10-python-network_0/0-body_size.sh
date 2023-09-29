#!/bin/bash
# script that sends reqest and get response

response_file=$(mktemp)
curl -s "$response_file" "$1"
size=$(stat -c %s "$response_file")
echo "$size"
rm "$response_file"

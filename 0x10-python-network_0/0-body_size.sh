#!/bin/bash
# script that sends reqest and get response
curl -Is "$1" | grep Content-Length | cut -f2 -d' '

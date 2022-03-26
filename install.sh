#!/usr/bin/env bash


opt=$1
if [[ $opt == "environment" ]]; then
  virtualenv environment
elif [[ $opt == "requirements" ]]; then
  source ./environment/bin/activate && python -m pip install -r requirements.txt
fi

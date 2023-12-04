#!/bin/bash

# Check if flag is passed
if [ $# -eq 0 ]; then
    echo "No arguments provided. Please provide a flag for either 'summary' or 'recommendations'."
    exit 1
fi

FLAG=$1
CONFIG_FILE="prompt-config.json"

# Check if config file exists
if [ ! -f $CONFIG_FILE ]; then
    echo "Configuration file not found! Please create a prompt-config.json file."
    exit 1
fi

# Read the prompt based on the flag
PROMPT=$(jq -r ".$FLAG // empty" $CONFIG_FILE)

# Check if prompt is empty or null
if [ -z "$PROMPT" ] || [ "$PROMPT" == "null" ]; then
    echo "Invalid flag or no prompt defined for this flag."
    exit 1
fi

# Run the Python script with the prompt
python src/main.py "$PROMPT"

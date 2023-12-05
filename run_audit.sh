#!/bin/bash

# Check if the correct number of arguments is passed
if [ $# -ne 2 ]; then
    echo "Invalid number of arguments. Usage: $0 [cloud_provider] [audit_type]"
    exit 1
fi

CLOUD_PROVIDER=$1
AUDIT_TYPE=$2
CONFIG_FILE="prompt-config.json"

# Validate the cloud provider
if [ "$CLOUD_PROVIDER" != "aws" ] && [ "$CLOUD_PROVIDER" != "azure" ]; then
    echo "Invalid cloud provider specified. Please specify either 'aws' or 'azure'."
    exit 1
fi

# Check if config file exists
if [ ! -f $CONFIG_FILE ]; then
    echo "Configuration file not found! Please create a prompt-config.json file."
    exit 1
fi

# Read the prompt based on the audit type
PROMPT=$(jq -r ".${AUDIT_TYPE} // empty" $CONFIG_FILE)

# Check if prompt is empty or null
if [ -z "$PROMPT" ] || [ "$PROMPT" == "null" ]; then
    echo "Invalid audit type or no prompt defined for this audit type."
    exit 1
fi

# Run the Python script with the cloud provider and the prompt
python src/main.py "$CLOUD_PROVIDER" "$PROMPT"

#!/bin/bash

PATH_TO_SCHEMA="$HOME/github-projects/the-brew-ha-ha-api-docs/"

# Generate the latest schema
echo "Generating the latest schema..."
python3 manage.py spectacular --color --file schema.yml
sleep .5

# Verify schema was generated successfully
if [ $? -ne 0 ]; then
    echo "Failed to generate schema" 
    exit 1
else
    echo "Schema generated!"
fi

# Copy the latest schema to the docs repo
echo "Copying schema to docs repo..."
sleep 1
cp schema.yml "$PATH_TO_SCHEMA"

# Verify transfer was successful
if [ -f "$PATH_TO_SCHEMA/schema.yml" ]; then
    echo "Schema successfully transferred"
else
    echo "Unsuccessful transfer" 
    exit 1
fi




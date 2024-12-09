#!/bin/bash

# Starting user story number
start_num=23

# Loop to create 5 folders and corresponding .py files
for i in $(seq 0 4); do
    # Calculate the current number, e.g., 0006, 0007, etc.
    num=$(printf "%04d" $(($start_num + $i)))
    
    # Folder name
    folder_name="User Story - $num"
    
    # Create the folder
    mkdir "$folder_name"

    
    # Optional: Print confirmation
    echo "Created folder: $folder_name "
done

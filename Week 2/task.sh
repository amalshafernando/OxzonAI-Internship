#!/bin/bash

# Starting user story number
start_num=6

# Loop to create 5 folders and corresponding .py files
for i in $(seq 0 4); do
    # Calculate the current number, e.g., 0006, 0007, etc.
    num=$(printf "%04d" $(($start_num + $i)))
    
    # Folder name
    folder_name="User Story - $num"
    
    # Create the folder
    mkdir "$folder_name"
    
    # Python file name (matching the folder name)
    python_file="$folder_name/User Story - $num.py"
    
    # Create the Python file inside the folder
    touch "$python_file"
    
    # Optional: Print confirmation
    echo "Created folder: $folder_name with Python file: $python_file"
done

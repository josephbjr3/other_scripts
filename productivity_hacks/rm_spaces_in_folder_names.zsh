#!/bin/zsh

# This scripts renames files and folders in the "~/Documents" directory, 
# replacing spaces with underscores for easier navigation in the CLI. 
# I'm still working on it. Right now, it only works one level down from the "~/Documents" directory

echo "Renaming files and folders in ~/Documents directory..."

# Loop through all files and folders in the ~/Documents directory
for file in ~/Documents/*; do
    if [[ -d "$file" ]]; then
        # If it's a directory, check if it contains spaces in the name
        if echo "$file" | grep -q " "; then
            # If it contains spaces, replace them with underscores
            new_name="$(echo "$file" | sed 's/ /_/g')"
            echo "Renaming directory: $file -> $new_name"
            mv -v "$file" "$new_name"
        fi
    elif [[ -f "$file" ]]; then
        # If it's a file, check if it contains spaces in the name
        if echo "$file" | grep -q " "; then
            # If it contains spaces, replace them with underscores
            new_name="$(echo "$file" | sed 's/ /_/g')"
            echo "Renaming file: $file -> $new_name"
            mv -v "$file" "$new_name"
        fi
    fi
done

echo "Done!"


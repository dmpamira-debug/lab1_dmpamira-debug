#!/bin/bash

FILE="grades.csv"
ARCHIVE="archive"
LOG="organizer.log"

if [ ! -d "$ARCHIVE" ]; then
    mkdir "$ARCHIVE"
fi

TIMESTAMP=$(date +"%Y%m%d-%H%M%S")

NEW_NAME="grades_$TIMESTAMP.csv"

mv "$FILE" "$ARCHIVE/$NEW_NAME"

touch "$FILE"

echo "$TIMESTAMP - moved $FILE to $ARCHIVE/$NEW_NAME" >> "$LOG"

echo " File archived successfully!"

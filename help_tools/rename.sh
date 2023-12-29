#!/bin/bash

# For Sorting directory
cd Sorting
for f in *.md; do mv "$f" "$(printf '%04d' $(echo $f | grep -o -E '[0-9]+'))_${f#*_}"; done

# For Linked_List directory
cd ../Linked_List
for f in *.md; do mv "$f" "$(printf '%04d' $(echo $f | grep -o -E '[0-9]+'))_${f#*_}"; done
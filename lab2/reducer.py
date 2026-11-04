#!/usr/bin/env python3
import sys

current_word = None
current_count = 0

for line in sys.stdin:

    line = line.strip()
    if not line:
        continue

    # maxsplit = 1
    word, count = line.split('\t', maxsplit=1)
    
    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print(current_word + "\t" + str(current_count))
        current_word = word
        current_count = count

if current_word:
    print(current_word + "\t" + str(current_count))
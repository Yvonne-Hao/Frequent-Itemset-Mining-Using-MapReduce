#!/usr/bin/env python
import sys
 
# maps words to their counts
reducer_dict = {}
 
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
 
    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue

    try:
        reducer_dict[word] = reducer_dict[word]+count
    except:
        reducer_dict[word] = count
 
# write the tuples to stdout
# Note: they are unsorted
for word in word2count.keys():
    print '%s\t%s'% ( word, word2count[word] )

for t in mapper:
    if t[0] in reducer_dict.keys():
        reducer_dict[t[0]] += 1
    else:
        reducer_dict[t[0]] = 1

result = []
for k in reducer_dict.keys():
    if reducer_dict[k] >= 2:
        result.append((k, reducer_dict[k]))



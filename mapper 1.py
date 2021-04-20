#!/usr/bin/env python

import sys
#!/usr/bin/env python
# 
# 
# 
# f=open("transaction.dat","r")
# content=f.read().splitlines()
# f.close()
# 
# 
# get all lines from stdin ---
# for line in sys.stdin:
#     remove leading and trailing whitespace---
#     item = line.strip()
# 
#     split the line into words ---
#     words = line.split()
#     
#     
#     output tuples [word, 1] in tab-delimited format---
#     for i in range(len(data)):
#       write the results to STDOUT (standard output);
#       what we output here will be the input for the
#       Reduce step, i.e. the input for reducer.py
#      
#       tab-delimited; the trivial word count is 1
#         j=i+1
#         while(j<len(data)):
#             try:
# 
#                 temp= data[i]+","+data[j]
#                 print('%s\t%s' % (temp, 1))
#                 j=j+1
#             except:
#                 continue
mapper = []
for line in open("transaction.dat", 'r'):

    words = line.rstrip().split()
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            mapper.append(((int(words[i]),int(words[j])),1))
 
reducer_dict = dict()
for t in mapper:
    if t[0] in reducer_dict.keys():
        reducer_dict[t[0]] += 1
    else:
        reducer_dict[t[0]] = 1
 
result = []
for k in reducer_dict.keys():
    if reducer_dict[k] >= 2:
        result.append((k, reducer_dict[k]))
 
 
print(result[:50])

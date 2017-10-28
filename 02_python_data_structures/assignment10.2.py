"""Assignment 10.2."""

# 10.2 Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages. You can pull the
# hour out from the 'From ' line by finding the time and then splitting the
# string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.

name = "D:/Dropbox/Coursera/python_for_everybody/02_python_data_structures/mbox-short.txt"
handle = open(name)

num_h = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        h = words[5].split(":")[0]
        num_h[h] = num_h.get(h, 0) + 1

lst = sorted([(v, k) for k, v in num_h.items()], reverse=True)

for k, v in lst:
    print(v, k)

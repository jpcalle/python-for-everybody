"""Assignment 9.4."""

# 9.4 Write a program to read through the mbox-short.txt and figure out who has
# the sent the greatest number of mail messages. The program looks for 'From '
# lines and takes the second word of those lines as the person who sent the
# mail. The program creates a Python dictionary that maps the sender's mail
# address to a count of the number of times they appear in the file. After the
# dictionary is produced, the program reads through the dictionary using a
# maximum loop to find the most prolific committer.

name = "D:/Dropbox/Coursera/python_for_everybody/02_python_data_structures/mbox-short.txt"
handle = open(name)

who_sent = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        who_tmp = words[1]
        who_sent[who_tmp] = who_sent.get(who_tmp, 0) + 1

who_max = None
how_many = None
for k, v in who_sent.items():
    if who_max is None or how_many < v:
        how_many = v
        who_max = k

print(who_max, how_many)
